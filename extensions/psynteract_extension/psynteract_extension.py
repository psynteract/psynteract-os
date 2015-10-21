#-*- coding:utf-8 -*-
from libopensesame.py3compat import *

from libopensesame import debug
from libqtopensesame.extensions import base_extension


class psynteract_extension(base_extension):

	"""Install psynteract backend"""

	def activate(self):

		"""
		desc:
			Is called when the extension is activated through the menu/ toolbar
			action.
		"""
		
		from libqtopensesame.dialogs.notification import notification
		welcome = notification(self.main_window,'On the next page, please input the URL of your couch db server followed by a database name.'
		'For example, if you have couch db installed on the machine you are currently using, you might enter: '
		'http://localhost:5984/psynteract')
		welcome.exec_()
		
		from libqtopensesame.dialogs.text_input import text_input
		psynteract_url = text_input(self.main_window)
		current_url = psynteract_url.get_input()
		
		from psynteract import install
		server_url = install(current_url)

		feedback = notification(self.main_window,'Your server is available at '+server_url)
		feedback.exec_()
		