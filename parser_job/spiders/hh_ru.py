import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem


class HhRuSpider(scrapy.Spider):

    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://spb.hh.ru/search/vacancy?area=1103&search_field=name&search_field=company_name&search_field=description&text=analyst'
    ]

    def parse(self, response):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        vacancies_links = response.xpath("//a[@data-qa='serp-item__title']/@href").getall()

        for link in vacancies_links:
            yield response.follow(link, method='GET', callback=self.vacancy_parse)

    def vacancy_parse(self, response:HtmlResponse):

        vacancy_name = response.css("h1::text").get()
        vacancy_salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancy_url = response.url

        yield ParserJobItem(
            name=vacancy_name,
            salary=vacancy_salary,
            url=vacancy_url,
            _id=response.url
        )
