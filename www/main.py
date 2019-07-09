from browser import document, alert, window
from browser.html import *
import sys

class CustomStdOut:

	console_output = document['console_output']

	def write(self, txt):

		lista = txt.split('\n')

		lista = ["<div style='width:98%'>{0}</div>".format(i) for i in lista]

		for i in lista:
			self.console_output.html += i
		
		self.console_output.scrollTop = self.console_output.scrollHeight - self.console_output.clientHeight



custom_stdout = CustomStdOut()
sys.stdout = custom_stdout
sys.stderr = custom_stdout

v = sys.implementation.version
print("Brython %s.%s.%s on %s %s"%(v[0], v[1], v[2], window.navigator.appName, window.navigator.appVersion))
print('<br/>---> sys.stdout')
print('---> sys.stderr')


