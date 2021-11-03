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
		
		self.experiment._connection.reassign_grouping(self.var.allow_rollover=='yes')
		
		self.experiment.var.current_role = self.experiment._connection.current_role
		self.experiment.var.current_grouping = self.experiment._connection.current_grouping
		current_partners = self.experiment._connection.current_partners
		for i,p in enumerate(current_partners):
			self.experiment.var.set('partner{:02d}_id'.format(i+1),p)		


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_reassign(psynteract_reassign, qtautoplugin):
	
	lazy_init = False
		
	def __init__(self, name, experiment, script=None):
		
		psynteract_reassign.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
