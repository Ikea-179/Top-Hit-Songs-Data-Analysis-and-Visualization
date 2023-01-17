# -*- coding: utf-8 -*-
import scrapy
import datetime

class Hot100Spider(scrapy.Spider):
    name = 'hot100'
    allowed_domains = ['billboard.com']
    start_urls = ['http://billboard.com/charts/hot-100//']

    def start_requests(self):
        yield scrapy.Request(url='https://billboard.com/charts/hot-100/2022-04-02', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })

    def roll_back_date(self, chart_date):
        if chart_date == datetime.date(1976, 7, 4):    
            previous_date = datetime.date(1976, 6, 26)

        elif chart_date == datetime.date(1962, 1, 6):
            previous_date = datetime.date(1961, 12, 25)

        else:
            roll_back = datetime.timedelta(weeks=1)
            previous_date = chart_date - roll_back

        previous_date = previous_date.strftime('%Y-%m-%d')
        return previous_date

    def parse(self, response):
        chart_date_string = (response.xpath(".//h2[starts-with(@class, 'c-heading larva  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-text-align-center lrv-u-margin-b-075')]/text()").get()).strip()[8:]
        chart_date = datetime.datetime.strptime(chart_date_string, '%B %d, %Y').date()
        
        hit = response.xpath("//div[starts-with(@class, 'o-chart-results-list-row-container')]")
        for i in range(len(hit)):
            if i == 0:
                yield {
                    'date': chart_date,
                    'title': (hit[i].xpath(".//h3[starts-with(@class, 'c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')]/text()").get()).strip(),
                    'artist': (hit[i].xpath(".//span[starts-with(@class, 'c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')]/text()").get()).strip(),
                    'rank': str(i + 1),
                    'last_week': (hit.xpath(".//span[starts-with(@class, 'c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet')]/text()")[0].get()).strip(),
                    'peak': (hit.xpath(".//span[starts-with(@class, 'c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet')]/text()")[1].get()).strip(),
                    'weeks': (hit.xpath(".//span[starts-with(@class, 'c-label  a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet')]/text()")[2].get()).strip()
                }
            else:
                yield {
                    'date': chart_date,
                    'title': (hit[i].xpath(".//h3[starts-with(@class, 'c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')]/text()").get()).strip(),
                    'artist': (hit[i].xpath(".//span[starts-with(@class, 'c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')]/text()").get()).strip(),
                    'rank': str(i + 1),
                    'last_week': hit[i].xpath(".//span[starts-with(@class, 'c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max')]/text()")[0].get().strip(),
                    'peak': hit[i].xpath(".//span[starts-with(@class, 'c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max')]/text()")[1].get().strip(),
                    'weeks': hit[i].xpath(".//span[starts-with(@class, 'c-label  a-font-primary-m lrv-u-padding-tb-050@mobile-max')]/text()")[2].get().strip()
                }
        previous_date_string = self.roll_back_date(chart_date)
        
        if int(previous_date_string.split('-')[0]) < 1960:
            return
        else:
            next_page_url = f'https://billboard.com/charts/hot-100/{previous_date_string}'
            yield scrapy.Request(next_page_url, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            })



