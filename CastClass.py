#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Kossakowski, Daniel
#
# Requirements:
# - pycurl (python-pycurl)
# - xmltodict (pip)

import socket
import pycurl
import xmltodict
from StringIO import StringIO


class ShoutCast1():

    def __init__(self, host, port, username, password):
        """
        Initialize socket and fill user credentials.

        :param host: FQDN or IP address of the server.
        :param port: Network port number.
        :param username: Admin username.
        :param password: Admin password.
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

        :param param: XML param to return.
        :return: string
        """
        url = "http://%s:%s/admin.cgi?pass=%s&mode=viewxml" % (self.host, self.port, self.password)

        storage = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.FOLLOWLOCATION, True)
        c.setopt(pycurl.USERAGENT, "Python CastClass (Mozilla Compatible)")
        c.setopt(pycurl.URL, url)
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        c.close()

        x = xmltodict.parse(storage.getvalue())
        return x[param]

    def check_presenter_online(self):
        if self.get_stream_status() == 0:
            return False
        else:
            if self.get_bitrate() == 0:
                return False
            else:
                return True

    def get_bitrate(self):
        return self.get_param('BITRATE')

    def get_stream_status(self):
        return self.get_param('STREAMSTATUS')

    def get_current_listeners(self):
        return self.get_param('CURRENTLISTENERS')

    def get_peak_listeners(self):
        return self.get_param('PEAKLISTENERS')

    def get_max_listeners(self):
        return self.get_param('MAXLISTENERS')

    def get_genre(self):
        return self.get_param('SERVERGENRE')

    def get_url(self):
        return self.get_param('SERVERURL')

    def get_server_title(self):
        return self.get_param('SERVERTITLE')

    def get_song_title(self):
        return self.get_param('SONGTITLE')

    def get_irc(self):
        return self.get_param('IRC')

    def get_aim(self):
        return self.get_param('AIM')

    def get_icq(self):
        return self.get_param('ICQ')


class ShoutCast2():

    def __init__(self, host, port, username, password):
        """
        Initialize socket and fill user credentials.

        :param host: FQDN or IP address of the server.
        :param port: Network port number.
        :param username: Admin username.
        :param password: Admin password.
        :return:
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.sock = socket.socket()

    def test_connection(self, timeout = 5):
        """
        Connect to ShoutCast vv server and return false on error or true on success.

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

    def get_param(self, param, stream = '1'):
        """
        Return value of requested param from ShoutCast v2 server.

        :param param: XML param to return.
        :param stream: Stream ID (ShoutCast2 can provide multiple streams, number starts from 1).
        :return: string
        """
        url = "http://%s:%s/admin.cgi?pass=%s&sid=%s&mode=viewxml" % (self.host, self.port, self.password, stream)
        
	storage = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.FOLLOWLOCATION, True)
        c.setopt(pycurl.USERAGENT, "Python CastClass (Mozilla Compatible)")
        c.setopt(pycurl.URL, url)
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        c.close()

	x = xmltodict.parse(storage.getvalue())
        return x['SHOUTCASTSERVER'][param]

    def check_presenter_online(self):
        if self.get_stream_status() == 0:
            return False
        else:
            if self.get_bitrate() == 0:
                return False
            else:
                return True

    def get_bitrate(self):
        return self.get_param('BITRATE')

    def get_stream_status(self):
        return self.get_param('STREAMSTATUS')

    def get_current_listeners(self):
        return self.get_param('CURRENTLISTENERS')

    def get_peak_listeners(self):
        return self.get_param('PEAKLISTENERS')

    def get_max_listeners(self):
        return self.get_param('MAXLISTENERS')

    def get_genre(self):
        return self.get_param('SERVERGENRE')

    def get_url(self):
        return self.get_param('SERVERURL')

    def get_server_title(self):
        return self.get_param('SERVERTITLE')

    def get_song_title(self):
        return self.get_param('SONGTITLE')
