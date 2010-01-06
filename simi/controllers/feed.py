import logging
import os
import re
import utils

from simi.lib.base import *
from simibase import *
from PIL import Image

from pylons import request, response

log = logging.getLogger(__name__)


class FeedController(SimiBaseController):

	def simi_index(self):
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"])
		albumcontext=utils.AlbumContext(albumdir)

		pics=albumcontext.get_images(include_private=False)

		c.title=albumdir.get_split_name()[1]
		c.subtitle=albumdir.get_split_name()[0]

		c.pics = pics
		c.albumdir = albumdir

		response.content_type='application/xhtml+xml'
		return render("/feed.mako")



