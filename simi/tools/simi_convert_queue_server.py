import os
import logging

from simi.lib.app_globals import *
from simi.lib import EXIF

g=Globals()

import SimpleXMLRPCServer


class SimiRPCServer:
	def __init__():
		pass

	def process_directory(dirname):
		return 0

	

server=SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000")
server.register_instance(SimiRPCServer))
