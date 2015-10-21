#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_push(item.item):
	"""Push data to server."""
	
	initial_view = 'controls'
	description = 'Push data to server.'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""

		self.var.auto_detect_variables = 'yes'
		self.var.custom_selection = ''
		
	def run(self):

		"""Runs the item."""
		
		if self.var.auto_detect_variables == u'yes':
			os_variables = dict(self.experiment.var.items())
		
		else:
			if self.var.custom_selection=='':
				os_variables = None
			
			else:
				selected_keys = self.custom_selection.replace(',', ' ')
				selected_keys = selected_keys.split()
				for var in selected_keys:
					if not var in self.experiment.var.vars():
						print('Custom variable "'+var+'" not found in experimental variables.')
				os_variables = dict((k, v) for k, v in self.experiment.var.items() if k in selected_keys)
			
		self.experiment._connection.doc['data']['os_variables'] = os_variables
				
		if self.experiment.offline == 'no':
			self.experiment._connection.push()


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)



class qtpsynteract_push(psynteract_push, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_push.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
		self.custom_interactions()

	def apply_edit_changes(self):

		"""Applies the controls."""

		if not qtautoplugin.apply_edit_changes(self) or self.lock:
			return False
		self.custom_interactions()
		return True

	def edit_widget(self):

		"""Refreshes the controls."""

		if self.lock:
			return
		self.lock = True
		w = qtautoplugin.edit_widget(self)
		self.custom_interactions()
		self.lock = False
		return w

	def custom_interactions(self):

		"""Activates the relevant controls and adjusts tooltips."""
		
		self.custom_variables_widget.setEnabled(self.var.auto_detect_variables=='no')
	