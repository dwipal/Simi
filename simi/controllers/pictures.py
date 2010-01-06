import logging

from simi.lib.base import *

log = logging.getLogger(__name__)

class PicturesController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        # return 'Hello World'
        return render('/list.mako')
