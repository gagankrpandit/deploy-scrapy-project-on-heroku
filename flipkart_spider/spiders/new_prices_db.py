import scrapy
import pandas as pd
from datetime import datetime

class DealAlertSpider(scrapy.Spider):
    name = 'new_prices_db'
    allowed_domains = ['flipkart.com']
    df = pd.read_csv('D:/webScraping/scrapy/flipkart_spider/flipkart_spider/priceHistory.csv')
    start_urls = list(df['url'])
    date_ = datetime.now().strftime("%m/%d/%Y, %H:%M")
    
    priceList = []
    def parse(self, response):
        price_ = response.css('._16Jk6d::text').extract()
        newPrice = price_[0].replace("₹", "").replace(",", "")
        self.priceList.append(newPrice)
        self.df[self.date_] = pd.Series(self.priceList)
        self.df.to_csv('priceHistory.csv', index=0)