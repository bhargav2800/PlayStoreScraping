from celery import shared_task
from google_play_scraper import app

from play_store_scraper.models import GameDetails, GamesPath, Categories, HistogramDetails, GameComents, GameScreenshots
from play_store_scraper.serializers import GameDeatailCreateSerializer


@shared_task
def scrape_game_details_task():
    """
    Function to send email to only accessible external user
    """

    GameDetails.objects.all().delete()
    for j in GamesPath.objects.all():
        fetched_game_details = app(j.app_detail_path)
        categories = []
        for i in fetched_game_details.get('categories'):
            category, _ = Categories.objects.get_or_create(name=i.get('name'))
            categories += [category.id]

        fetched_game_details['categories'] = categories
        game_detail_serializer = GameDeatailCreateSerializer(data=fetched_game_details)
        game_detail_serializer.is_valid(raise_exception=False)
        instance = game_detail_serializer.save(package=j)

        HistogramDetails.objects.bulk_create(
            [HistogramDetails(**{'game_detail': instance, 'histogram': item}) for item in
             fetched_game_details.get('histogram', [])])
        GameComents.objects.bulk_create([GameComents(**{'game_detail': instance, 'comment': item}) for item in
                                         fetched_game_details.get('comments', [])])
        GameScreenshots.objects.bulk_create(
            [GameScreenshots(**{'game_detail': instance, 'screenshot': item}) for item in
             fetched_game_details.get('screenshots', [])])

    return True
