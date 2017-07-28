#!/usr/bin/env python
# -*- coding: utf-8 -*-

import make_config
from colorama import init
import logmodule
import connection
import ConfigParser
import make_country
import os

init(autoreset=True)
logmodule.start_log()


class Joinner(object):

    def writeconfig(self):
        w = make_config.RunConf()
        w.write_conf()

    def open_config_ftp(self):

        parser = ConfigParser.RawConfigParser()
        parser.read('config.ini')
        ftp_name = parser.get('CONFIG', 'ftp')
        return ftp_name

    def open_config_continents(self):

        parser = ConfigParser.RawConfigParser()
        parser.read('config.ini')
        c = dict(parser.items('CONTINENTS'))
        l = dict(parser.items('DIR_LOC'))
        return c, l

    def joiner_all(self, conf_continents, con_ftp):

        pwd = os.getcwd()
        list_file = os.listdir(pwd)

        for item in list_file:
            if item.endswith('.txt'):
                os.remove(item)

        try:
            open_con = connection.FTP()
            ftp_con = open_con.open_connection_all(con_ftp)
            ftp_con.login()
            conf_dir = sorted(conf_continents[0].items())
            conf_name = sorted(conf_continents[1].items())

            for i in range(0, len(conf_continents[1].items())):
                f = open("%s_%s.txt" % (conf_dir[i][0],conf_name[i][1]), 'wb')
                print (conf_name[i][1])
                ftp_con.cwd(conf_dir[i][1])
                print ftp_con.pwd()
                ftp_con.retrbinary('RETR %s' % conf_name[i][1], f.write)

        except Exception as e:
            print e

if __name__ == "__main__":

    x = Joinner()
    x.writeconfig()
    x.joiner_all(x.open_config_continents(), x.open_config_ftp())
    y = make_country.CountryCode()
    y.make_country_name()


