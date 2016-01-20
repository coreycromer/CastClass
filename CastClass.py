#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Kossakowski, Daniel
#

import socket
import pycurl


class ShoutCast():

    def __init__(self, host, port, username, password):
        """
        Initialize socket and fill user credentials.

        :param host:
        :param port:
        :param username:
        :param password:
        :return:
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.sock = socket.socket()

    def test_connection(self, timeout = 5):
        """
        Connect to ShoutCast v1 server and return false on error or true on success.

        :param timeout:
        :return:
        """
        # Host and port must be a Tuple!
        self.sock.settimeout(timeout)

        try:
            self.sock.connect((self.host, self.port))
            return True
        except:
            return False

    def get_param(self, param):
        """
        Return value of requested param from ShoutCast v1 server.

        :param param:
        :return: string
        """
        c = pycurl.Curl()
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.URL, "http://%s:%s/admin.cgi?pass=%s&mode=viewxml HTTP/1.1\r\n" % (self.host, self.port, self.password))
        c.perform()

        self.sock.send("User-Agent: Python CastClass")


c = ShoutCast('127.0.0.1', 80, '', '')
print c.connect(1)
print c.getParam('jurek')

"""
/*
* Zwracanie danej pozycji, oto ich lista:
* CURRENTLISTENERS - ilość aktualnych słuchaczy
* PEAKLISTENERS - dotychczasowy rekord liczby słuchaczy
* MAXLISTENERS - maksymalna ilość słuchaczy
* SERVERGENRE - rodzaj serwera
* SERVERURL - adres URL strony
* SERVERTITLE - nazwa serwera
* SONGTITLE - nazwa utworu aktualnie odtwarzanego
* IRC - identyfikator IRC
* AIM - identyfikator AIM
* ICQ - identyfikator ICQ
* STREAMSTATUS - status strumienia
* BITRATE - jakość nadawania
*/

"""