from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from play_store_scraper.models import GamesPath, GameDetails, Categories, HistogramDetails, GameScreenshots, GameComents
from play_store_scraper.serializers import GamesDetailPathSerializer, GameDeatailCreateSerializer, \
    GameDeatailListSerializer
from scrapy_scraper.scrapy_scraper.spiders.play_store_spider import PlayStoreSpiderSpider
import scrapydo
from play_store_scraper.tasks import scrape_game_details_task


# Create your views here.
class PlayStoreScrapGamesUrl(CreateAPIView):
    """
        Used to scrap game detail urls using scrapy.
    """
    queryset = GamesPath.objects.all()
    serializer_class = GamesDetailPathSerializer

    def post(self, request, *args, **kwargs):
        scrapydo.setup()
        scrapydo.run_spider(PlayStoreSpiderSpider)
        return Response({"mag": "Packages has been scraped successfuly..."}, status=status.HTTP_200_OK)


class PlayStoreScrapGamesDetails(ListCreateAPIView):
    """
        Used to scrap game detail urls using scrapy.
    """
    serializer_class = GameDeatailListSerializer
    queryset = GameDetails.objects.all().prefetch_related('game_histograms', 'game_screenshots', 'game_comments',
                                                          'categories')

    def post(self, request, *args, **kwargs):
        scrape_game_details_task.delay()
        return Response({"mag": "Scraping started ..."}, status=status.HTTP_200_OK)
