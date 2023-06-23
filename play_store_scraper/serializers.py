from rest_framework import serializers
from play_store_scraper.models import GamesPath, GameDetails, HistogramDetails, GameComents, GameScreenshots, Categories


class GamesDetailPathSerializer(serializers.ModelSerializer):
    """
        Serializer for games path model.
    """

    class Meta:
        model = GamesPath
        fields = ["id", "app_detail_path"]


class HistogramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistogramDetails
        fields = ['id', 'histogram']


class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameComents
        fields = ['id', 'comment']


class ScreenShotsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScreenshots
        fields = ['id', 'screenshot']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class GameDeatailCreateSerializer(serializers.ModelSerializer):
    """
        Serialzier for create games details view.
    """
    released = serializers.DateField(allow_null=True, input_formats=['%Y-%m-%d', '%b %d, %Y'])

    class Meta:
        model = GameDetails
        fields = ['id', 'title', 'description', 'descriptionHTML', 'summary', 'installs', 'minInstalls', 'realInstalls',
                  'score', 'ratings', 'reviews', 'price', 'free', 'currency', 'sale', 'originalPrice',
                  'saleText', 'offersIAP', 'inAppProductPrice', 'developer', 'developerId', 'developerEmail',
                  'developerWebsite', 'developerAddress', 'privacyPolicy', 'genre', 'genreId', 'categories', 'icon',
                  'headerImage', 'video', 'videoImage', 'contentRating', 'contentRatingDescription', 'adSupported',
                  'containsAds', 'released', 'updated', 'version', 'appId', 'url']


class GameDeatailListSerializer(serializers.ModelSerializer):
    """
        Serialzier for games details view.
    """
    categories = CategorySerializer(many=True)
    game_histograms = HistogramDetailSerializer(many=True)
    game_screenshots = ScreenShotsDetailSerializer(many=True)
    game_comments = CommentsDetailSerializer(many=True)

    class Meta:
        model = GameDetails
        fields = ['id', 'title', 'description', 'descriptionHTML', 'summary', 'installs', 'minInstalls', 'realInstalls',
                  'score', 'ratings', 'reviews', 'price', 'free', 'currency', 'sale', 'originalPrice',
                  'saleText', 'offersIAP', 'inAppProductPrice', 'developer', 'developerId', 'developerEmail',
                  'developerWebsite', 'developerAddress', 'privacyPolicy', 'genre', 'genreId', 'icon',
                  'headerImage', 'video', 'videoImage', 'contentRating', 'contentRatingDescription', 'adSupported',
                  'containsAds', 'released', 'updated', 'version', 'appId', 'url', 'categories', 'game_histograms',
                  'game_screenshots', 'game_comments']
