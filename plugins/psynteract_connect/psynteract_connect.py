#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame.exceptions import osexception
from libopensesame import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from libqtopensesame.misc import _

# Import libraries
from psynteract import Connection

class psynteract_connect(item.item):
	"""Setup connection with session."""
	
	initial_view = 'controls'
	description = 'Setup connection with session.'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""

		self.var.server = ''
		self.var.db_name = 'psynteract'
		self.var.design = 'perfect_stranger'
		self.var.group_size = 2
		self.var.roles = ''
		self.var.groupings_needed = 1
		self.var.ghosts = 'no'
		self.var.identical_rseed = 'no'
		self.var.display_messages = 'yes'
		self.var.offline = 'no'
		
		
	def run(self):

		"""Runs the item."""
		
		self.experiment.var.offline = self.var.offline
		
		if self.var.roles=='':
			self._roles = None
		else:
			self._roles = self.var.roles.replace(',', ' ')
			self._roles = self._roles.split()
		
		if self.var.display_messages == 'yes':
			from openexp.canvas import canvas
			message_canvas= canvas(self.experiment)
			message_canvas.text('Connecting with the session...')
			message_canvas.show()
		
		self.experiment._connection = Connection(
			server_uri=self.var.server,db_name=self.var.db_name,
			client_name=self.experiment.subject_nr,
			design=self.var.design, group_size=self.var.group_size,
			groupings_needed=self.var.groupings_needed,
			roles=self._roles,
			ghosts=self.var.ghosts=='yes',
			initial_data={'os_status':{},'os_variables':{}},
			offline=self.var.offline=='yes')
		
		if self.identical_rseed == u'yes':
			print 'Set random seed depending on psynteract session'
			import random
			random.seed(self.experiment._connection.session)
			
		if self.var.display_messages == 'yes':
			self.experiment.clock.sleep(1000)
			message_canvas= canvas(self.experiment)
			message_canvas.text('Waiting for the session to start...')
			message_canvas.show()
		
		self.experiment._connection.await(lambda doc: doc['status'] == 'running', check="session")
		self.experiment.var.current_role = self.experiment._connection.current_role
		
		if self.var.display_messages == 'yes':
			self.experiment.clock.sleep(1000)


	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)


class qtpsynteract_connect(psynteract_connect, qtautoplugin):
	
	def __init__(self, name, experiment, script=None):
		
		psynteract_connect.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)
