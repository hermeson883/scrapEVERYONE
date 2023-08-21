import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        #Deserialize the api for a python object
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')
        for quote in quotes:
            data = {
                'author': quote['author']['name'],
                'text' : quote['text'],
                'tag' : quote['tags']
            }
            yield data