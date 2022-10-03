import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem


class SjRuSpider(scrapy.Spider):
    name = 'sj_ru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://spb.superjob.ru/vakansii/buhgalter.html']

    def parse(self, response):
        next_page = response.xpath("//a[contains(@class,' f-test-link-Dalshe')]/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacancies_links = response.xpath("//span[@class = '_9fIP1 _249GZ _1jb_5 QLdOc']/a[contains(@class, '_1IHWd f-test-link')]/@href").getall()

        for link in vacancies_links:
            yield response.follow(link, method='GET', callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):

        vacancy_name = response.css("h1::text").get()
        vacancy_salary = response.xpath("//span[@class = '_2eYAG _1nqY_ _249GZ _1dIgi']/text()").getall()
        vacancy_url = response.url

        yield ParserJobItem(
            name=vacancy_name,
            salary=vacancy_salary,
            url=vacancy_url,
            _id=response.url
        )
