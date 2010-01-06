"""The application's Globals object"""
import re

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application
    """

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the 'g'
        variable
        """
	self.albums_dir="/mnt/data/xpslaptop/dwipal/Pictures"
	self.temp_dir="/mnt/data/cache/simi_thumbs"
	self.thumbs_url="http://dwipal.dyndns.org/cache/simi_thumbs"
	self.path_re=re.compile(r"[^A-Za-z0-9]")

	self.exiv_cmd="/usr/bin/exiv2"

	self.simi_passwords=['simiboy','research1']
	self.simi_private_passwords=['simiboy']


