import scrapy
import json

class ResortSpider(scrapy.Spider):
    name = "resort"
    allowed_domains = ["ski-resort.info"]

    def start_requests(self):
        # open links.txt
        with open('E:\\prj\\Python\\skidbscraper\\links.txt') as f:
            resort_links = f.readlines()
            for link in resort_links:
                yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        # {
        #     'name': name,
        #     'rating': rating if rating is not None else 'N/A'
        #     'country': country,
        #     'county': county,
        #     'elevation': elevation,
        #     'slope_lengths': {
        #         'total': total_slope_length,
        #         'blue': blue_slope_length,
        #         'red': red_slope_length,
        #         'black': black_slope_length,
        #         'additional': additional_slope_length
        #     },
        #     'pass_prices': {
        #         'adult': adult_pass_price,
        #         'youth': youth_pass_price,
        #         'child': child_pass_price,
        #     },
        #     'season_start': season_interval[0].strip(),
        #     'season_end': season_interval[1].strip(),
        #     'opening_time': open_hours[0].strip(),
        #     'closing_time': open_hours[1].strip(),
        #     'neighbouring_towns': neighbouring_towns
        # }

        return_json = json.loads('{}')
        return_json['name'] = response.css('div.col-sm-10 > h1 > span.item > span.fn::text').get()
        rating = response.css('div.rating-list.js-star-ranking.stars-big::attr(data-rank)').get()
        if rating is not None:
            return_json['rating'] = rating

        country = response.css("div.col-md-8 > div.panel-simple.more-padding > p > a:nth-of-type(2)::text").get()
        county = response.css("div.col-md-8 > div.panel-simple.more-padding > p > a:nth-of-type(1) > strong::text").get()
        if country is not None:
            return_json['country'] = country
        elif county is not None:
            # if there is no county information then the country is the first element
            return_json['country'] = county
            county = None

        if county is not None:
            return_json['county'] = county

        elevation = response.css('#selAlti::text').get()
        if elevation is not None:
            return_json['elevation'] = elevation.split('(')[0].strip()

        # slope lengths
        total_slope_length = response.css('#selSlopetot::text').get()
        if total_slope_length is not None:
            return_json['slope_lengths'] = {}
            return_json['slope_lengths']['total'] = total_slope_length.split(':')[1].removesuffix('km').strip()

        blue_slope_length = response.css('#selBeginner::text').get()
        if blue_slope_length is not None:
            return_json['slope_lengths']['blue'] = blue_slope_length.removesuffix('km').strip()

        red_slope_length = response.css('#selInter::text').get()
        if red_slope_length is not None:
            return_json['slope_lengths']['red'] = red_slope_length.removesuffix('km').strip()

        black_slope_length = response.css('#selAdv::text').get()
        if black_slope_length is not None:
            return_json['slope_lengths']['black'] = black_slope_length.removesuffix('km').strip()

        additional_slope_length = response.css('#selExpert::text').get()
        if additional_slope_length is not None:
            return_json['slope_lengths']['additional'] = additional_slope_length.removesuffix('km').strip()

        adult_pass_price = response.css('#selTicketA::text').get()
        if adult_pass_price is not None:
            return_json['pass_prices'] = {}
            return_json['pass_prices']['adult'] = adult_pass_price

        youth_pass_price = response.css('#selTicketY::text').get()
        if youth_pass_price is not None:
            return_json['pass_prices']['youth'] = youth_pass_price

        child_pass_price = response.css('#selTicketC::text').get()
        if child_pass_price is not None:
            return_json['pass_prices']['child'] = child_pass_price

        season_interval = response.css('#selSeason::text').get()
        if season_interval is not None:
            split_interval = season_interval.split('-')
            return_json['season_start'] = split_interval[0].strip()
            return_json['season_end'] = split_interval[1].strip()

        open_hours = response.css("#selOperationtimes::text").get()
        if open_hours is not None:
            split_open_hours = open_hours.split('-')
            return_json['opening_time'] = split_open_hours[0].strip()
            return_json['closing_time'] = split_open_hours[1].strip()

        neighbouring_towns = response.css("#selLinkCustomer > ul.detail-overview-citylist > li > a::text").getall()
        if neighbouring_towns is not []:
            return_json['neighbouring_towns'] = neighbouring_towns


        if len(return_json) > 2:
            yield return_json
        else:
            pass
