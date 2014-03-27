# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utils.utils import (
		get_id, 
		clear_id, 
		print_hex_data,
		get_frequency,
		is_printable,
		extract_text,
	)

DATA_TYPES_ENUM = ['text','archive','image','audio','video','ciphered','raw','fs']

data_types = {}

map(lambda x: data_types.update(
	{

		x.encode('utf-8'):
			{
				'id':get_id(),
				'size': -1,
				'format': None,
				'source': None,
				'provider': None
			}
	}

	),DATA_TYPES_ENUM)


# print data_types


class Data(object):
	"""
	Abstract class describing the main aims of this framework
	"""

	def __init__(self):
		self._data = None
		self._debug = 0
		self._modified = True
		self._is_text = None
		self._size = -1
		self._spectr = {}

	def get_data(self):
		return self._data

	def size(self):
		if self.modified():
			self._size = len(self._data)
		return self._size

	def modified(self):
		return self._modified

	def analize(self):
		raise Exception('Abstract method call!')

	def __speedanalize(self):
		raise Exception('Abstract method call!')

	def __analize(self):
		raise Exception('Abstract method call!')

	def __deepanalize(self):
		raise Exception('Abstract method call!')

	def detecttype(self):
		raise Exception('Abstract method call!')

	def detectformat(self):
		raise Exception('Abstract method call!')

	def print_(self):
		raise Exception('Abstract method call!')

	def __str__(self):
		raise Exception('Abstract method call!')

	def __repr__(self):
		raise Exception('Abstract method call!')

	def load(self,source):
		raise Exception('Abstract method call!')

	def save(self,destination):
		raise Exception('Abstract method call!')

	def convert(self,format):
		raise Exception('Abstract method call!')

	def __hex__(self):
		return print_hex_data(self._data,pprint = False)

	def __len__(self):
		return len(self._data)

	def as_hex(self):
		return self.__hex__()

	def is_text(self):
		if self.modified():
			self._is_text = is_printable(self._data)
		return self._is_text

	def as_text(self):
		return extract_text(self._data)

	def spectr(self, show = False):
		"""
		Discover the symbol frequency
		"""
		if (self._spectr is None) or (self.modified()):
			self._spectr = get_frequency(self._data, pprint = False)
		return self._spectr


class UnknownFile(Data):

	def __init__(self,filename):
		Data.__init__(self)
		self._data = open(filename,'rt').read()
		if not self.is_text():
			self.data = open(filename,'rb').read()



__author__ = "Andriy Vasyltsiv"