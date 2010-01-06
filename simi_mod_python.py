#http://mydjangoblog.com/2009/03/30/django-mod_python-and-virtualenv/


import os, sys
pcwd = os.path.dirname(__file__)


from paste.script.util.logging_config import fileConfig
fileConfig('%s/deployment.ini' % pcwd)

from paste.deploy import loadapp
application = loadapp('config:%s/deployment.ini' % pcwd) 


from paste.modpython import handler
