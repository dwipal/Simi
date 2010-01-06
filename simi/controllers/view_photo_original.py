import logging

from simi.lib.base import *
from simibase import *
import utils

log = logging.getLogger(__name__)

class ViewPhotoOriginalController(SimiBaseController):

	def simi_index(self):
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"])
		pic=utils.AlbumPicture(albumdir, request.params["img"])


		# read the original file
		f=open(pic.get_full_original_path(), "rb")
		
		# Return the JPG response of the image
		response.headers['Content-type'] = "image/jpeg"	
		return f.read()
		
		
		

