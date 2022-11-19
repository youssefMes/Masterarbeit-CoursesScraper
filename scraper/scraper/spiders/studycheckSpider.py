from ast import parse
from json import load
from pprint import pprint
from this import d
from scrapy import Spider, Request
from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader
from scraper.items import CourseItem
from pprint import pprint

class StudycheckspiderSpider(Spider):
    name = 'studycheckSpider'
    allowed_domains = ['www.studycheck.de']
    start_urls = ['https://www.studycheck.de/suche?rt=2&q=&c=1&modal=1']
    portal_name = 'studyCheck'
    def parse(self, response):
      for course in response.css('div.rfv1-media-layout__row.rfv1-media-layout__row--relative.rfv1-display--flex')[0:1]:
        url = course.css('a::attr(href)').extract_first()
        yield Request('https://www.studycheck.de/studium/medieninformatik/lmu-muenchen-9392', callback = self.parse_item_informations)
    
    def parse_item_informations(self, response):
        cards = response.xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' courses-details ')]/div[contains(@class, 'card')]"
            )
        informations = {
            'university': response.xpath('normalize-space(//div[@class="institute-text"]/a/text())').extract_first()
        }
        for card in cards:
            informations = {**informations, **self.parse_card(card)} 
        
        loader = ItemLoader(item=CourseItem(), response=response)
        loader.default_output_processor = TakeFirst()
        loader.add_xpath('name', 'normalize-space(//h1[@class="course-title"]/text())')
        loader.add_value('link', response._url)
        loader.add_value('information', informations)

        yield loader.load_item()
        #yield Request(response._url + '/bewertungen', callback = self.parse_item_evaluations)

    def parse_item_evaluations(self, response):
        loader = ItemLoader(item=CourseItem(), response=response)
        
       
        yield loader.load_item()
    
    def parse_card(self, card):
        blocTitle = card.xpath("normalize-space(header[contains(@class, 'card-header')]/h2/text())").extract_first()
        
        informations = {}
        match blocTitle:
            case 'Vollzeitstudium':
                informations = {
                    'study_form': 'Vollzeitstudium',
                    **self.parse_card_informations(card)
                }
            case 'Studiengangdetails':
                description = card.xpath("normalize-space(div[contains(@class, 'card-block')]/p/text())").extract_first()
                if (description == ''):
                    informations = self.parse_card_informations(card)
                else:
                    informations = {**informations, 'description': description}
        return informations

    @staticmethod
    def parse_card_informations(card):
        informationDivs = card.xpath("//div[contains(@class, 'card-row') and contains(@class, 'card-row--no-border')]")
        mapping = {
            'Regelstudienzeit': 'study_periode',
            'Studienbeginn': 'study_start',
            'Abschluss': 'degree',
            'Unterrichtssprachen': 'languages',
            'Standorte': 'city',
        }
        excluded = ['Bewertung', 'Bewertungen', 'Weiterempfehlung']
        informations = {}
        for div in informationDivs:
            label = div.xpath("normalize-space(div[contains(@class, 'card-row-label')]//text())").extract_first()
            if label in excluded:
                continue
            value = ''
            if label in ['Inhalte', 'Voraussetzungen']:
                value = ''.join(div.xpath("div[contains(@class, 'card-row-content')]//*").getall())
            else:
                value = div.xpath("normalize-space(div[contains(@class, 'card-row-content')])").extract_first()

            if label in mapping:    
                informations[mapping[label]] = value
                continue
            if 'other_informations' not in informations:
                informations['other_informations'] = {}
            informations['other_informations'][label] = value
        
        return informations