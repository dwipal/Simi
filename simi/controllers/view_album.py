import logging
import os
import re
import utils

from simi.lib.base import *
from simibase import *
from PIL import Image


log = logging.getLogger(__name__)


class ViewAlbumController(SimiBaseController):

	def simi_index(self):
		flush = ('flush' in request.params)
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"], flush_album=flush)
		albumcontext=utils.AlbumContext(albumdir)

		c.albumdir=albumdir
		c.pics=albumcontext.get_images(include_private=self.get_session().is_private_session())
		c.sub_albums=albumcontext.sub_albums
		
		log.debug("Starting to generate thumbnails...")
		if c.pics and not c.pics[-1].is_thumb_exists():
			albumcontext.generate_all_thumbnails()
		log.debug ("Thumbnail generation completed.")

		c.title=albumdir.get_split_name()[1]
		c.subtitle=albumdir.get_split_name()[0]

		return render("/view_album.mako")


