import scrapy
import pandas as pd
# import datetime

class FkrtSpiderSpider(scrapy.Spider):
    name = 'fkrt_spider'
    allowed_domains = ['flipkart.com']
    # start_urls = ['https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']

    start_urls = []
    for i in range(4):
        start_urls.append(f'https://www.flipkart.com/search?q=convection+microwave+oven&sid=j9e%2Cm38%2Co49&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_14_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=convection+microwave+oven%7CMicrowave+Ovens&requestId=73592145-5e38-4297-8c82-7a60124db736&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DMorphy%2BRichards&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&page={i+1}')

    def parse(self, response):
        
        url_ = response.css('._1fQZEK::attr(href)').extract()
        url = []
        for i in range(len(url_)):
            url.append('https://www.flipkart.com' + url_[i])

        title = response.css('._4rR01T::text').extract()
        price_ = response.css('._1_WHN1::text').extract()
        price = []
        for i in range(len(price_)):
            price.append(price_[i].replace(",", "").replace("₹", ""))
        
        zipped = zip(url, title, price)
        zipped = list(zipped)
        url, title, price = zip(*zipped)

        dict_ = {
            'url': url,
            'title': title,
            'price': price
        }

        df = pd.DataFrame(dict_)
        print(df.head())
        df.to_csv('D:/webScraping/scrapy/flipkart_spider/flipkart_spider/scrapedData.csv', mode='a',index=False)
    
    
        

