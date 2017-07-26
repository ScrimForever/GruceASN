# !/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date,timedelta
import ConfigParser


yesterday = (date.today() - timedelta(days=1))
yesterday = yesterday.strftime("%Y%m%d")
today = date.today().strftime("%Y%m%d")

class RunConf(object):

    def write_conf(self):
        self.parser = ConfigParser.RawConfigParser()

        self.parser.add_section('CONFIG')
        self.parser.set('CONFIG', 'FTP', 'ftp.lacnic.net')
        self.parser.add_section('CONTINENTS')
        self.parser.set("CONTINENTS", 'AFRINIC','/pub/stats/afrinic')
        self.parser.set("CONTINENTS", 'APINIC', '/pub/stats/apnic')
        self.parser.set("CONTINENTS", 'ARIN','/pub/stats/arin')
        self.parser.set("CONTINENTS", 'LACNIC','/pub/stats/lacnic')
        self.parser.set("CONTINENTS", 'RIPENCC','/pub/stats/ripencc')
        self.parser.add_section('DIR_LOC')
        self.parser.set("DIR_LOC", 'afrinic', 'delegated-afrinic-extended-%s' % today)
        self.parser.set("DIR_LOC", 'apnic', 'delegated-apnic-extended-%s' % today)
        self.parser.set("DIR_LOC", 'arin', 'delegated-arin-extended-%s' % today)
        self.parser.set("DIR_LOC", 'lacnic', 'delegated-lacnic-extended-%s' % yesterday)
        self.parser.set("DIR_LOC", 'ripencc', 'delegated-ripencc-extended-%s' % yesterday)
        with open('config.ini', 'wb') as cf:
            self.parser.write(cf)




