from django.db import models


# Create your models here.
class GamesPath(models.Model):
    """
    role model
    """
    app_detail_path = models.CharField(max_length=255)

    class Meta:
        db_table = "GamesPaths"
        verbose_name = "GamesPaths"
        indexes = [
            models.Index(fields=["app_detail_path"]),
        ]

    def __str__(self):
        return f"{self.app_detail_path}-{self.id}"


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)


class GameDetails(models.Model):
    package = models.ForeignKey(GamesPath, on_delete=models.CASCADE, related_name="package_details")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    descriptionHTML = models.TextField(null=True)
    summary = models.TextField(null=True)
    installs = models.CharField(max_length=255, null=True)
    minInstalls = models.CharField(max_length=255, null=True)
    realInstalls = models.CharField(max_length=255, null=True)
    score = models.FloatField(default=0.0)
    ratings = models.BigIntegerField(null=True)
    reviews = models.BigIntegerField(null=True)
    price = models.IntegerField(null=True)
    free = models.BooleanField(default=False)
    currency = models.CharField(max_length=20)
    sale = models.BooleanField(default=False)
    originalPrice = models.IntegerField(null=True)
    saleText = models.TextField(null=True)
    offersIAP = models.BooleanField(default=False)
    inAppProductPrice = models.CharField(max_length=255, null=True)
    developer = models.CharField(max_length=255, null=True)
    developerId = models.CharField(max_length=255, null=True)
    developerEmail = models.EmailField(null=True)
    developerWebsite = models.URLField(null=True)
    developerAddress = models.TextField(null=True)
    privacyPolicy = models.URLField(null=True)
    genre = models.CharField(max_length=255, null=True)
    genreId = models.CharField(max_length=255, null=True)
    categories = models.ManyToManyField(Categories, related_name="game_category")
    icon = models.URLField(null=True)
    headerImage = models.URLField(null=True)
    video = models.URLField(null=True)
    videoImage = models.URLField(null=True)
    contentRating = models.CharField(max_length=255, null=True)
    contentRatingDescription = models.TextField(null=True)
    adSupported = models.BooleanField(default=False)
    containsAds = models.BooleanField(default=False)
    released = models.DateField(null=True)
    updated = models.BigIntegerField(null=True)
    version = models.CharField(max_length=255, null=True)
    appId = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True)


class HistogramDetails(models.Model):
    game_detail = models.ForeignKey(GameDetails, on_delete=models.CASCADE, related_name="game_histograms")
    histogram = models.BigIntegerField()


class GameScreenshots(models.Model):
    game_detail = models.ForeignKey(GameDetails, on_delete=models.CASCADE, related_name="game_screenshots")
    screenshot = models.URLField()


class GameComents(models.Model):
    game_detail = models.ForeignKey(GameDetails, on_delete=models.CASCADE, related_name="game_comments")
    comment = models.TextField()
