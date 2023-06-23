from django.contrib import admin
from play_store_scraper.models import GamesPath, Categories, GameScreenshots, GameDetails, GameComents

# Register your models here.
admin.site.register(GamesPath)
admin.site.register(Categories)
admin.site.register(GameScreenshots)
admin.site.register(GameDetails)
admin.site.register(GameComents)