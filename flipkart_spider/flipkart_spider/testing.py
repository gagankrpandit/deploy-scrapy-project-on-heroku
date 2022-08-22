import pandas as pd

df = pd.read_csv('D:/webScraping/scrapy/flipkart_spider/flipkart_spider/priceHistory.csv')

for i in range(len(df)):
    url = df.iloc[i, 0]
    priceHistory = list(df.iloc[i,2:len(df.columns)-1].dropna())
    priceHistory = [x for x in priceHistory if x]
    newPrice = df.iloc[i,len(df.columns)-1]
    minPrice = min(priceHistory)
    avgPrice = round(sum(priceHistory)/len(priceHistory))
    
    if newPrice < minPrice:
        print(f'Lowest ever @Rs: {newPrice}\nProduct link: {url}\n')
    elif newPrice == minPrice:
        print(f'Currently minimum price @Rs: {newPrice}\nProduct link: {url}')
    else:
        pass