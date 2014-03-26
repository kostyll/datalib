# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utils.utils import (
		get_id, 
		clear_id, 
		print_hex_data,
		get_frequency,
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
		self.data = None
		self.debug = 0
		self.modified = True

	def analize(self):
		raise Exception('Abstract method call!')

	def _speedanalize(self):
		raise Exception('Abstract method call!')

	def _analize(self):
		raise Exception('Abstract method call!')

	def _deepanalize(self):
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
		return print_hex_data(self.data,pprint = False)

	def __len__(self):
		return len(self.data)

	def as_hex(self):
		return self.__hex__()

	def as_text(self):
		pass

	def spectr(self, show = False):
		"""
		Discover the symbol frequency
		"""
		return get_frequency(self.data, pprint = False)


__author__ = "Andriy Vasyltsiv"