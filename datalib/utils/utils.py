# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from StringIO import StringIO
from io import BytesIO
import pprint

pp = pprint.PrettyPrinter(indent=4)

# from datalib import IOError

global_id = -1

def get_id():
	global global_id
	global_id += 1
	return global_id

def clear_id():
	global global_id
	global_id = -1


def print_hex_data(data,offset=0,length=-1, pprint=True):
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
			if byteindex != 0:
				addr = hex(byteindex-16)
				buffer.write(
					"\n{0:8s} {1:52s} | {2:18s} [{3}]".format(
						addr,symbols,string.encode('ascii','replace'),options)
					)
				addr = symbols = string = options = ""
			# byteindex = byteindex+16
		if byteindex % 8 == 0:
			symbols +='  '
		symbols+=hex(ord(symbol)).split('x')[1]+' '
		string += symbol.encode('ascii',"ignore")
		byteindex += 1
	if symbols != "":
		addr = hex(byteindex-len(string))
		buffer.write(
			"\n{0:8s} {1:52s} | {2:18s} [{3}]".format(
				addr,symbols,string.encode('ascii','replace'),options)
			)
	buffer.read()
	print (buffer.buf)
	return buffer.buf


def get_frequency(data,offset=0,length=-1, pprint=True):
	result = {}
	for symbol in data[offset:len(data) if length == -1 else length]:
		result.update({ord(symbol):result.get(ord(symbol,0))+1})
	if pprint:
		pp.pprint(result)
	return result



__author__ = "Andriy Vasyltsiv"