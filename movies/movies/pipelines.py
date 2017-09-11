# -*- coding: utf-8 -*-
import json
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviesPipeline(object):
    def __init__(self):
        # elf.filename = codecs.open("test.txt", "w", "utf-8")
        pass

    def process_item(self, item, spider):
        fp = codecs.open("oumei.txt", "a")
        name = item['name']
        link_ftp = item['link_ftp']
        score = item['score']
        if score >= 7.0:

            line = "name: %s \tscore: %.1f\n url: %s \n"%(name, score, link_ftp)
            print line
            # print type(line)
            fp.write(line)
            return item

