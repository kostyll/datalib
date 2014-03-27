# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nose import with_setup
import sys
import pprint
import yaml


sys.path.insert(0, '/home/andrew/workspace/w/datalib/datalib/')
sys.path.insert(1,r'F:\work\datalib\datalib')
# print sys.path

from utils.utils import (
        print_hex_data,
        get_frequency,
        is_printable,
        extract_text,
        show_spectr,
    )

from datalib.datalib import (
        Data, UnknownFile
    )

pp = pprint.PrettyPrinter(indent=4)


class TestBase(object):

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


class TestUtils(TestBase):


    def test_print_hex_data_ascii(self):
        print "test print_hex_data ascii"
        print_hex_data('werwerasde23454@!@#@$243534534werwerwerwer;l,dvsd')

    def test_print_hex_data(self):
        print "test print_hex_data"
        print_hex_data('werwerasdeфывівІ23454@!@#@$243534534werwerwerwer;l,dvsd')

    def test_get_frequency(self):
        print "test_get_frequency"
        assert get_frequency("aabcddd") == {ord('a'):2,ord('b'):1, ord('c'):1,ord('d'):3}


    def test_is_printable(self):
        print "test is_printable"
        assert is_printable('sdfwer@serfwerfwerwe') == True
        assert is_printable('ЬY§asdasd') == False

    def test_extract_text(self):
        data = yaml.load(open("./test/data/tests.yaml","r"))
        for item in data['printable_text']:
            item = eval(item)
            value = extract_text(item[0])
            print ("v='{}', r='{}'".format(value,item[1]))
            assert value == item[1]
        for item in data['mixed_text']:
            item = eval(item)
            value = extract_text(item[0])
            print ("v='{}', r='{}'".format(value,item[1]))
            assert value == item[1]


class TestUnknownFile(TestBase):

    def test_file_spectr(self):
        uf = UnknownFile('./test/data/tests.yaml')
        spectr = uf.spectr()
        assert spectr is not None
        show_spectr(spectr)



# if __name__ == "__main__":
#     test = TestCase()
#     test.test_print_hex_data()
#     test.test_print_hex_data_ascii()