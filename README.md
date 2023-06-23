# PlayStoreScraping
Play Store Scrapping with Django \
https://play.google.com/store/games?hl=en&amp;gl=US

# Steps to run the project
1. Take a pull of repo.
2. Command for installing requirements : **pip install -r requirements.txt**
3. Command for start celery and server : **python3 manage.py runserver_celery**
4. There are 3 urls :\
   (1) Scrape game package names using scrapy : http://127.0.0.1:8000/playstore/ (POST)\
   (2) Scrape game details using google-play-scraper : http://127.0.0.1:8000/playstore/details/ (POST)\
   (3) List Scraped data : http://127.0.0.1:8000/playstore/details/ (GET)