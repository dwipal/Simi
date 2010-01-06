
# Ways to access:
# Based on b64 url
# Based on actual directory name

# Need as output
# Actual directory name (for originals)
# Thumbnail directory 
# Full Path for each thumbnail, original, etc

import os, subprocess, traceback, time, re, shutil
from datetime import datetime
import logging

from PIL import Image

from simi.lib.app_globals import *
from simi.lib import EXIF

g=Globals()

log = logging.getLogger(__name__)


class AlbumContext:
	albumdir=None
	pics=None
	sub_albums=None
	browse_index=-1

	def __init__(self, albumdir):
		self.albumdir=albumdir

	def get_images(self, include_private=False):
		if self.pics==None:
			img_files=os.listdir(self.albumdir.get_full_album_path())

			pics=[]
			sub_albums=[]
			for i in img_files:

				if '.private' in i.lower() and not include_private:
					log.debug("skipping private file %s"%i)
					continue

				full_path=os.path.join(self.albumdir.get_full_album_path(),i)
				if os.path.isdir(full_path):
					sub_albums.append(AlbumDirectory(full_path))
					continue
				if not i.lower().endswith(".jpg"):
					continue

				pic=AlbumPicture(self.albumdir, i)
				pics.append(pic)
			self.pics=pics
			self.sub_albums=sub_albums

		return self.pics
		

	def set_current_image(self, pic):
		pics=self.get_images()
		for i in range(len(pics)):
			if pics[i] == pic:
				self.browse_index=i
				break
		
	def get_browse_index(self):
		return self.browse_index

	def generate_all_thumbnails(self):
		pics = self.get_images()
		for p in pics:
			p.generate_preview()
			p.generate_thumbnail()


	
class AlbumDirectory:
	dirname=None
	shortname=None
	full_thumb_path=None
	split_name=None

	def __init__(self, dirname=None, urlname=None, flush_album=False):
		if urlname:
			self.set_url_name(urlname)
		if dirname:
			self.set_dir_name(dirname)

		if flush_album:
			self.delete_thumb_directory()

		self.generate_thumb_directory()


	def set_dir_name(self, dirname):
		self.dirname=dirname

	def get_dir_name(self):
		return self.dirname

	def set_url_name(self, urlname):
		self.set_dir_name(urlname.decode("base64"))
		
	def get_url_name(self):
		e=self.dirname.encode("base64")
		return e.replace('\n','')

	def get_album_zip_url(self):
		return "download_album/make_zip?dir=%s"%self.get_url_name()

	def get_zip_download_url(self):
		base_thumb_url=os.path.join(g.thumbs_url, self.get_thumb_name())
		return os.path.join(base_thumb_url, "all.zip")	

	def get_album_url(self):
		return "view_album?dir=%s"%self.get_url_name()

	def get_album_feed_url(self):
		return "feed?dir=%s"%self.get_url_name()

	def get_thumb_name(self):
		return g.path_re.sub("", self.dirname)

	def get_full_zip_path(self):
		return os.path.join(self.get_full_thumb_path(), "all.zip")

	def get_full_original_path(self):
		return os.path.join(g.albums_dir, self.dirname)

	def get_full_thumb_path(self):
		if not self.full_thumb_path:
			self.full_thumb_path=os.path.join(g.temp_dir, self.get_thumb_name())
		return self.full_thumb_path

	def get_full_album_path(self):
		return os.path.join(g.albums_dir, self.dirname)


	def delete_thumb_directory(self):
		if os.path.exists(self.get_full_thumb_path()):
			shutil.rmtree(self.get_full_thumb_path())

	def generate_thumb_directory(self):
		if not os.path.exists(self.get_full_thumb_path()):
			os.mkdir(self.get_full_thumb_path())
	
	def get_split_name(self):
		if not self.split_name:
			r=re.compile("([0-9]+-[0-9]+-[0-9]+) (.+)")
			clean_name=os.path.basename(self.dirname)
			m=r.match(clean_name)
			if m :
				self.split_name=(m.group(1), m.group(2))
			else:
				self.split_name=("",clean_name)
		
		return self.split_name

		
	def __cmp__(self, other):
		s1,s2 = self.get_split_name()
		o1,o2 = other.get_split_name()

		dtcmp = 0
			
		if s1!='' and o1!='':
			try:
				dtcmp=cmp(datetime.strptime(s1, '%Y-%m-%d'), datetime.strptime(o1, '%Y-%m-%d'))
			except Exception, e:
				log.error( 's1: [%s], o1: [%s]'%(s1,o1))
				raise e
				pass
		elif s1!='' or o1 !='':
			if s1 != '':
				return -1
			else:
				return 1

		if dtcmp == 0:
			return cmp(s2,o2)
		else:
			return dtcmp




class AlbumPicture:
	filename=None
	albumdir=None
	img_error=False
	exif_data=None
	resize_time=0
	exif_time=0

	def __init__(self, albumdir, filename):
		self.albumdir=albumdir
		self.filename=filename
		self.base_thumb_url=os.path.join(g.thumbs_url, albumdir.get_thumb_name())

	def __eq__(self, other):
		return (self.filename==other.filename and self.albumdir==other.albumdir)

	def get_thumb_name(self):
		return "t_" + self.filename

	def get_preview_name(self):
		return "p_" + self.filename

	def get_full_original_path(self):
		return os.path.join(self.albumdir.get_full_original_path(), self.filename)

	def get_full_thumb_path(self):
		return os.path.join(self.albumdir.get_full_thumb_path(), self.get_thumb_name())

	def get_full_preview_path(self):
		return os.path.join(self.albumdir.get_full_thumb_path(), self.get_preview_name())


	def is_thumb_exists(self):
		return os.path.exists(self.get_full_thumb_path())

	def is_preview_exists(self):
		return os.path.exists(self.get_full_preview_path())

	def get_thumb_url(self):
		self.generate_thumbnail()
		return os.path.join(self.base_thumb_url, self.get_thumb_name())	

	def get_image_url(self):
		self.generate_preview()
		return os.path.join(self.base_thumb_url, self.get_preview_name())

	def get_preview_url(self):
		return self._make_image_page_url("view_photo")

	def get_original_image_url(self):
		return self._make_image_page_url("view_photo_original")

	def _make_image_page_url(self, servlet_name):
		return "%s?dir=%s&img=%s"%(servlet_name, self.albumdir.get_url_name(), self.filename)

	def generate_thumbnail(self):
		self._resize_image(self.get_full_thumb_path(), 80, 80, True)

	def generate_preview(self):
		self._resize_image(self.get_full_preview_path(), 800, 600, False)

	def get_exif_data(self):
		raise "Not supported right now"

		f=open(self.get_full_original_path(), "rb")
		return EXIF.process_file(f, debug=False)
		try:
			f=open(self.get_full_original_path(), "rb")
			ex=EXIF.process_file(f, debug=False)
			log.info("Exif Data: " + str(ex))
			return ex
		except Exception, e:
			log.error("Error while getting exif data for %s: %s"%(self.get_full_original_path(), str(e)))

		return {}

	def get_exif_data_dump(self):
		t1=time.time()
		if not self.exif_data:
			try:
				s=subprocess.Popen([g.exiv_cmd, self.get_full_original_path()], stdout=subprocess.PIPE)
				self.exif_data=s.communicate()[0]
			except Exception, e:
				self.exif_data="EXIF data not available: %s"%str(e)
		
		self.exif_time=time.time()-t1
		return self.exif_data

	def get_exif_data_map(self):
		dump=self.get_exif_data_dump()

		if not dump:
			return None

		# Exif data is:
		# Parameter Name: Value
		# One per line

		# Separate each line
		dump=dump.split('\n')

		dump_map={}
		for row in dump:
			row=row.split(":")
			if len(row)==2:
				dump_map[row[0].strip()] = row[1].strip()
		return dump_map
	

	def _resize_image(self, dest_path, width, height, is_thumbnail):
		if not os.path.exists(dest_path):
			t1=time.time()
			log.debug("generating %s, %i"%(dest_path, width))
	
			# Use the preview image to generate thumbnail, so we have to play with smaller file size.
			source_filename=self.get_full_original_path()
			if width < 100 and os.path.exists(self.get_full_preview_path()):
				source_filename=self.get_full_preview_path()
		
			try:
				im=Image.open(source_filename)
				newsize=im.size
				w,h=im.size

				if w >= h:
					# Horizontal image
					if w > width:
						sf=float(width)/float(w)
						newsize=(width, int(h*sf))
				else:
					if h > height:
					# Vertical image
						sf=float(height)/float(h)
						newsize=(int(w*sf), height)

						if is_thumbnail:
								# Have the width slightly larger
								minwidth=float(width)/1.3
								if newsize[0] < minwidth:
										# New width is too small, make it wider.
										sf=float(minwidth)/float(w)
										newsize=(minwidth, int(h*sf))
							

				im=im.resize(newsize, Image.ANTIALIAS)
				im.save(dest_path)
			except Exception, e:
				log.error( "Error while resizing image: " + str(e))
				self.img_error=True
			self.resize_time=time.time()-t1
			log.info("generated %s, %i completed in %f "%(dest_path, width, self.resize_time))
		




