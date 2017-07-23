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

    def open_config_ftp(self):

        parser = ConfigParser.RawConfigParser()
        parser.read('config.ini')
        ftp_name = parser.get('CONFIG', 'ftp')
        return ftp_name

    def open_config_continents(self):

        parser = ConfigParser.RawConfigParser()
        parser.read('config.ini')
        x = dict(parser.items('CONTINENTS'))
        return x

    def joiner_all(self, conf_continents, con_ftp):
        try:
            open_con = connection.FTP()
            ftp_con = open_con.open_connection_all(con_ftp)
            ftp_con.login()

            for i in range(0, len(conf_continents.items())):
                print conf_continents.items()[i]
                ftp_con.cwd(conf_continents.values()[i])
                try:
                    ftp_con.retrbinary('RETR delegated-%s-extended-%s.txt' % (conf_continents.keys()[i],Joinner.today), open('%s_%s.txt' % (conf_continents.keys()[i],Joinner.today), 'w'))

                except Exception as e:
                    print e
                break
        except Exception as e:
            print e
    #def joiner_nic_all_contry(self,country):

    #def joiner_nic_country(self,continent,country):

if __name__ == "__main__":

    x = Joinner()
    print x.joiner_all(x.open_config_continents(), x.open_config_ftp())



