#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib


class FTP(object):

    def open_connection_all(self, ftp_name):

        try:
            self.ftp = ftplib.FTP(ftp_name)
            return self.ftp
        except Exception as e:
            print (e)