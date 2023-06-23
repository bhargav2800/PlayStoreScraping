from django.urls import path
from play_store_scraper.views import PlayStoreScrapGamesUrl, PlayStoreScrapGamesDetails

urlpatterns = [
    path('', PlayStoreScrapGamesUrl.as_view(), name='list_games'),
    path('details/', PlayStoreScrapGamesDetails().as_view(), name='fetch_game_details')
]
