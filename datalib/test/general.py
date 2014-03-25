# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose import with_setup
import sys

sys.path.insert(0, '/home/andrew/workspace/w/datalib/datalib/')
# print sys.path

from utils.utils import print_hex_data

class TestCase(object):

    def setup(self):
        print ("Initializing {}".format(__file__))

    def teardown(self):
        print ("End {}".format(__file__))

    @classmethod
    def setup_class(cls):
        print ("setup class {}".format(__name__))

    @classmethod
    def teardown_class(cls):
        print ("teardown class {}".format(__name__))

    def test_InitNose(self):
        print "test_InitNose"
        assert 2+2 == 4

    def test_print_hex_data_ascii(self):
        print "test print_hex_data ascii"
        print_hex_data('werwerasde23454@!@#@$243534534werwerwerwer;l,dvsd')

    def test_print_hex_data(self):
        print "test print_hex_data"
        print_hex_data('werwerasdeфывівІ23454@!@#@$243534534werwerwerwer;l,dvsd')


if __name__ == "__main__":
    test = TestCase()
    test.test_print_hex_data()
    test.test_print_hex_data_ascii()