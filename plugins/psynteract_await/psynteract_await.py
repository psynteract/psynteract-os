#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_await(item.item):
	"""Wait for other clients."""
	
	initial_view = 'controls'
	description = 'Wait for other clients.'
	
	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		self.var.additional_wait = 1000


	def run(self):

		"""Runs the item."""
		
		current_await = self.name
		if self.name in self.experiment._connection.doc['data']['os_status']:
			self.experiment._connection.doc['data']['os_status'][current_await]+=1
		else:
			self.experiment._connection.doc['data']['os_status'][current_await]=1
		
		current_status = self.experiment._connection.doc['data']['os_status'][current_await]
		
		if self.experiment.var.offline == 'no':
		
			self.experiment._connection.push()

			def check_awaits(doc):
				check = False
				if current_await in doc['data']['os_status']:
					check = doc['data']['os_status'][current_await]>=current_status
				return check
				
			self.experiment._connection.await(check_awaits)
		
		
		if self.experiment.var.offline == 'no':
			self.experiment._connection.push()

		self.experiment.clock.sleep(self.var.additional_wait)


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_await(psynteract_await, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_await.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
