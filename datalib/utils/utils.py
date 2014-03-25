# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from StringIO import StringIO
from io import BytesIO
from datalib improt IOError

global_id = -1

def get_id():
	global global_id
	global_id += 1
	return global_id

def clear_id():
	global global_id
	global_id = -1


def print_hex_data(data,offset=0,length=-1):
	try:
		length = len(data)
	except Exception, e:
		print e
		raise IOError

	if isinstance(data,(str, )):
		pass
	if isinstance(data,(StringIO, )):
		pass
	if isinstance(data,(BytesIO, )):
		pass

	addr = symbols = string = options = ""
	byteindex = 0
	buffer = StringIO('')
	for symbol in data[offset:length]:
		if byteindex % 16 == 0:
			buffer.write('\n')
		if byteindex % 8 == 0:
			symbols
		string += symbol





__author__ = "Andriy Vasyltsiv"