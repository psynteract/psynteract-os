#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_communicate(item.item):
	"""Push data to server, wait for responses of other clients, and get their data."""
	
	initial_view = 'controls'
	description = 'Push data to server, wait for responses of other clients, and get their data.'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		
		self.var.auto_detect_variables = 'yes'
		self.var.custom_selection = ''
		self.var.display_message = 'no'
		self.var.waiting_message = ''
		self.var.additional_wait = 1000
		self.var.own_var_as_test = 'yes'

		
	def run(self):

		"""Runs the item."""
		
		# prepare push (actual push comes later)
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
				
		
		# wait
		
		current_wait = self.name
		if self.name in self.experiment._connection.doc['data']['os_status']:
			self.experiment._connection.doc['data']['os_status'][current_wait]+=1
		else:
			self.experiment._connection.doc['data']['os_status'][current_wait]=1
		
		current_status = self.experiment._connection.doc['data']['os_status'][current_wait]
		
		if self.var.display_message == 'yes':
			from openexp.canvas import canvas
			message_canvas= canvas(self.experiment)
			message_canvas.text(self.var.waiting_message)
			message_canvas.show()
		
		
		if self.experiment.var.offline == 'no':
		
			self.experiment._connection.push()

			def check_waits(doc):
				check = False
				if current_wait in doc['data']['os_status']:
					check = doc['data']['os_status'][current_wait]>=current_status
				return check
				
			self.experiment._connection.wait(check_waits)
		
		
		# push data to server
		if self.experiment.var.offline == 'no':
			self.experiment._connection.push()

		
		# get data
		
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
		
		
		# additional wait time		
		self.experiment.clock.sleep(self.var.additional_wait)
		

	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)



class qtpsynteract_communicate(psynteract_communicate, qtautoplugin):
	
	lazy_init = False
		
	def __init__(self, name, experiment, script=None):
		
		psynteract_communicate.__init__(self, name, experiment, script)
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
		self.waiting_message_widget.setEnabled(self.var.display_message=='yes')
	