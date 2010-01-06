import logging

from simi.lib.base import *
from simi.lib import EXIF
from simibase import *
import utils
import time

log = logging.getLogger(__name__)

class ViewPhotoController(SimiBaseController):

	def simi_index(self):
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"])
		pic=utils.AlbumPicture(albumdir, request.params["img"])
		pic.generate_preview()

		acontext=utils.AlbumContext(albumdir)
		acontext.set_current_image(pic)


		c.pic=pic
		c.albumdir=albumdir
		c.albumcontext=acontext
		c.total_servlet_time=time.time() - self.start_time

		c.title=albumdir.get_split_name()[1]
		c.subtitle=albumdir.get_split_name()[0]

		r=render("/view_photo.mako")
		return r


