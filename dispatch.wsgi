# Add the virtual Python environment site-packages directory to the path
import site

# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/mnt/wwwroot/simi/egg-cache'

# Load the Pylons application
from paste.deploy import loadapp
application = loadapp('config:/mnt/wwwroot/simi/production.ini')
