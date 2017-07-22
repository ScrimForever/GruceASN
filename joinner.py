#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta
import re
import os
from colorama import init
from colorama import Fore
import logmodule
import connection
import ConfigParser

init(autoreset=True)
logmodule.start_log()


class Joinner(object):

    yesterday = (date.today() - timedelta(days=1))
    yesterday = yesterday.strftime("%Y%m%d")
    today = date.today().strftime("%Y%m%d")

    def open_config(self):

        configParser = ConfigParser.RawConfigParser()
        configParser.read('config.ini')
        ftp = configParser.get('CONFIG', 'ftp')
        print ftp











    def joiner_all(self):

        con = connection.FTP()


    #def joiner_nic_all_contry(self,country):

    #def joiner_nic_country(self,continent,country):

if __name__ == "__main__":
    x = Joinner()
    print x.yesterday
    print x.today
    print x.open_config()
    print "finish"

