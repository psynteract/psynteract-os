#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _


class psynteract_wait(item.item):
	"""Wait for other clients."""
	
	initial_view = 'controls'
	description = 'Wait for other clients.'
	
	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		self.var.display_message = 'no'
		self.var.waiting_message = ''
		self.var.additional_wait = 1000	


	def run(self):

		"""Runs the item."""
		
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
		
		
		if self.experiment.var.offline == 'no':
			self.experiment._connection.push()

		self.experiment.clock.sleep(self.var.additional_wait)


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_wait(psynteract_wait, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_wait.__init__(self, name, experiment, script)
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
		
		self.waiting_message_widget.setEnabled(self.var.display_message=='yes')
	