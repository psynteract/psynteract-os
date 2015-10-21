#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_get(item.item):
	"""Get data from server."""
	
	initial_view = 'controls'
	description='Get data from server.'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""

		self.var.own_var_as_test = 'yes'
		

	def run(self):

		"""Runs the item."""
		
		if self.experiment.var.offline == 'no':
			current_partners = self.experiment._connection.current_partners
			for i,p in enumerate(current_partners):
				other_data = self.experiment._connection.get(p)['data']['os_variables']
				for var in other_data:
					self.experiment.var.set('partner{:02d}_{}'.format(i+1,var),other_data[var])
		
		if self.experiment.var.offline == 'yes' and self.var.own_var_as_test == 'yes':
			group_size = self.experiment._connection.group_size
			other_data = self.experiment._connection.doc['data']['os_variables']
			if other_data is not None:
				for i in range(1,group_size):
					for var in other_data:
						self.experiment.var.set('partner{:02d}_{}'.format(i,var),other_data[var])
		

	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)



class qtpsynteract_get(psynteract_get, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_get.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
		