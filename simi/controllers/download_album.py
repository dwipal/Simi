import logging
import os
import re
import utils
import zipfile

from simi.lib.base import *
from simibase import *
from PIL import Image


log = logging.getLogger(__name__)


class DownloadAlbumController(SimiBaseController):

	def make_zip(self):
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"])
		
		if not (os.path.exists(albumdir.get_full_zip_path())):
				# Create the zip file in thumbnails directory
				temp_zf=albumdir.get_full_zip_path()+".tmp"
				zf=zipfile.ZipFile(temp_zf, "w")

				# Switch directory to source files, so it doesnt have nasty folders
				curr_dir=os.getcwd()
				os.chdir(albumdir.get_full_original_path())

				# Add all the files there
				retstr = ""
				picfiles=os.listdir('.')
				for pic in picfiles:
						#skip the .zip files
						if '.zip' in pic:
							continue
						
						if(os.path.isfile(pic)):
								retstr=retstr +  pic + ", "
								zf.write(pic)
				zf.close()

				os.rename(temp_zf, albumdir.get_full_zip_path())
				os.chdir(curr_dir)

		#return redirect_to(str("/download_album/get_zip?dir=%s"%request.params["dir"])) 
		return redirect_to(albumdir.get_zip_download_url())

	def get_zip(self):
		albumdir=utils.AlbumDirectory(urlname=request.params["dir"])

		# read the original file
		f=open(albumdir.get_full_zip_path(), "rb")
		
		# Return the JPG response of the image
		response.headers['Content-type'] = 'application/zip'	
		response.headers['Content-Disposition'] = 'attachment; filename="all.zip"'
		return f.read()

