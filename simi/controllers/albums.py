import logging
import os
import re

from simi.lib.base import *
from simibase import *
import utils

log = logging.getLogger(__name__)
replace_chars_re=re.compile(r"[^A-Za-z0-9]")
date_re=re.compile(r"[0-90-90-90-9]-")

class AlbumEntry:
	dir_name=""
	short_name=""
	
	def __init__(self, dir_name):
		self.dir_name=dir_name
		self.short_name=replace_chars_re.sub("_",dir_name)
		self.short_name=dir_name.encode("base64")

class AlbumsController(SimiBaseController):

	def simi_index(self):
		# Return a rendered template
		#   return render('/some/template.mako')
		# or, Return a response
		self.get_directories(include_private=self.get_session().is_private_session())
		return render('/albums.mako')

	def get_directories(self, include_private=False):
		albums = os.listdir(g.albums_dir)

		album_entries=[]

		for a in albums:
			if os.path.isdir(os.path.join(g.albums_dir, a)):
				if '.private' in a.lower() and not include_private:
					continue

				album_entries.append(utils.AlbumDirectory(dirname=a))

		album_entries = sorted(album_entries, reverse=True)
		c.albums=album_entries

	def is_login_required(self):
		return True


	
		
