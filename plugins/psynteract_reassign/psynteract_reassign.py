#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_reassign(item.item):
	"""Assign client to next grouping."""
	
	initial_view = 'controls'
	description = 'Assign client to next grouping.'
	
	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		
		self.var.allow_rollover = 'yes'



	def run(self):

		"""Runs the item."""
		
		if self.experiment.var.offline == 'no':
			self.experiment._connection.reassign_grouping(self.var.allow_rollover=='yes')
			self.experiment.var.current_role = self.experiment._connection.current_role


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_reassign(psynteract_reassign, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_reassign.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
