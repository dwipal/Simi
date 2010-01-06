#!/usr/bin/python


import logging
from paste.deploy import loadapp, appconfig
from pylons import config
from simi.config.environment import load_environment

logging.basicConfig(level=logging.INFO,
	filename='/tmp/simi.log',
	filemode='a')
logging.info('SIMI dispatch initialized.\n')


CONFIG_FILE="config:/mnt/wwwroot/simi/production.ini"
conf = appconfig(CONFIG_FILE)
load_environment(conf.global_conf, conf.local_conf)

app = loadapp(CONFIG_FILE)
logging.debug("*** Dispatch method called. ****")

# Deploy it using FastCGI
if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(app).run()


