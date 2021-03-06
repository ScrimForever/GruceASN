#!/usr/bin/env python
# -*- coding: utf-8 -*-

import make_config
import connection
import ConfigParser
import make_country
import os
import time


class Joinner(object):

    def cleanfiles(self):
        dir = os.getcwd()
        dirlist = os.listdir(dir)
        for i in dirlist:
            if i.endswith('.txt'):
                os.remove(i)
                print "Removendo:  %s" % i

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
        return (c,l)

    def joiner_all(self, conf_continents, con_ftp):
        try:
            open_con = connection.FTP()
            ftp_con = open_con.open_connection_all(con_ftp)
            ftp_con.login()
            conf_dir = sorted(conf_continents[0].items())
            conf_name = sorted(conf_continents[1].items())

            for i in range(0, len(conf_continents[1].items())):
                f = open("%s_%s.txt" % (conf_dir[i][0],conf_name[i][1][-8:]), 'wb')
                ftp_con.cwd(conf_dir[i][1])
                ftp_con.retrbinary('RETR %s' % conf_name[i][1], f.write)

        except Exception as e:
            print e


    #def joiner_nic_all_contry(self,country):

    #def joiner_nic_country(self,continent,country):

if __name__ == "__main__":

    y = make_country.CountryCode()
    y.make_country_name()
    x = Joinner()
    x.cleanfiles()
    time.sleep(5)
    x.writeconfig()
    x.joiner_all(x.open_config_continents(), x.open_config_ftp())

