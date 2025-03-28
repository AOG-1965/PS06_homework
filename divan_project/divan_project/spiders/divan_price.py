import scrapy
import pandas as pd

class DivanPriceSpider(scrapy.Spider):
    name = "divan_price"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        data = []

        for divan in divans:
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            url = divan.css('a').attrib['href']

            data.append({'name': name, 'price': price, 'url': url})

        # Сохраняем данные в CSV
        df = pd.DataFrame(data)
        df.to_csv('divan_data.csv', index=False)
        self.log(f"Данные сохранены в 'divan_data.csv'")