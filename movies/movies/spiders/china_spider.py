# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from movies.items import MoviesItem
from bs4 import BeautifulSoup
import json
import lxml
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

class Myspider(scrapy.Spider):
    name = 'china'
    allowed_domains = ['ygdy8.com']
    bash_url = 'http://www.ygdy8.com/html/gndy/oumei/list_7_'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1,173):
            url = self.bash_url + str(i) + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        a = BeautifulSoup(response.text, 'lxml').find_all(class_="ulink")

        # print len(a)
        domain = "http://www.ygdy8.com"
        url_list = []
        for i in a:
            url = str(i['href'])
            if not url == "/html/gndy/dyzz/index.html":
                if not url == "/html/gndy/jddy/index.html":
                    url_list.append(domain + url)
                    # print domain + url
        # print len(url_list)
        for i in url_list:
            yield Request(i, callback=self.get_info)

    def get_info(self, response):

        bs = BeautifulSoup(response.text, 'lxml')
        name = bs.find('h1').text
        # print name.string
        link_ftp = bs.find("tbody").find("a")['href']
        # print link_ftp

        item = MoviesItem()
        item['name'] = name
        item['link_ftp'] = link_ftp


        score = bs.find("div", id="Zoom").find("p")

        test = '评分'.decode("utf-8")
        s = re.compile("评分(.*?)user")
        try:
            b = s.findall(str(score))[0].split(" ")[1].split('/')[0]
            score = float(b)
            item['score'] = score
        except Exception as err:
            item['score'] = 0.0
        # print item
        yield item


