#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_heartbeat(item.item):
	"""Send heartbeat to server."""
	
	initial_view = 'controls'
	description = 'Send heartbeat to server.'
	
	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		pass


	def run(self):

		"""Runs the item."""
		
		self.experiment._connection.heartbeat()

	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_heartbeat(psynteract_heartbeat, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_heartbeat.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
