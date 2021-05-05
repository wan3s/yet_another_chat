import gettext
import sys
import os.path

"""
Deployment test module.

:copyright: KorotkovBS, 2021
"""

datapath = os.path.dirname(sys.argv[0])
gettext.install('app', os.path.join('po'), names=("ngettext",))

def say_hello():
	"""
	Dumb function.
	
	:return: nothing
	"""
	print(_("Hello world!"))
