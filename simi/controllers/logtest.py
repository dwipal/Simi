import logging

from simi.lib.base import *

log = logging.getLogger(__name__)

class LogtestController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
	request.environ['wsgi.errors'].write('logging to wsgi.errors!\nfor 2 lines\n')
	log.error("My first pylons log ERROR message in a real log file!\nand in another line\n")
	
	logging.basicConfig(level=logging.INFO,
		filename='/tmp/simi.log',
		filemode='a')
	logging.debug('A debug message\nacross 2 lines...\n')
	
        return 'Check the Logs'
