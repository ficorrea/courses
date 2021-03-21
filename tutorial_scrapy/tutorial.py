import scrapy

class MyScrap(scrapy.Spider):
    name = 'scrap'

    
    start_urls =  ['http://quotes.toscrape.com/page/1/']

    """ def parse(self, response):
        scrapy.Request(url=response.url, callback=self.parse)    
        response.css('.quote') """
    
    def parse(self, response):
        quotes = response.css('.quote')      
        citacoes = [i.css('.text::text').get() for i in quotes]
        autores = [i.css('.author::text').get() for i in quotes]
        urls = [i.css('span a::attr(href)').get() for i in quotes]
        for c, a, u in zip(citacoes, autores, urls):
            print('{} - {} -- {}'.format(c, a, u))



# nome
# url
# citação
# lista de tags