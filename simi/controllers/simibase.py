import logging

from simi.lib.base import *


log = logging.getLogger(__name__)


class SimiSession:
	_session_created = False
	_private_session = False
	
	def __init__(self, request):
		if request.cookies.get("simi_session", "") in ["yes", "private"]:
			self.set_session_created()

		if request.cookies.get("simi_session", "") in ["private"]:
			self.set_private_session()

	def is_session_created(self):
		return self._session_created

	def set_session_created(self):
		self._session_created = True
		

	def is_private_session(self):
		return self._private_session

	def set_private_session(self):
		self._private_session = True

	def create_session(self, passwd):
		if passwd in g.simi_passwords:
			if passwd in g.simi_private_passwords:
				response.set_cookie("simi_session","private")
			else:
				response.set_cookie("simi_session","yes")
		else:
			raise SessionException("Incorrect password.")

			

	def delete_session(self):
		response.set_cookie("simi_session", expires=0)


class SimiBaseController(BaseController):
	simi_session = None

	def index(self):
		lr = self.is_login_required()


		if self.is_login_required():
			if not self.get_session().is_session_created():
				redirect_to("login?next=%s"%request.path_info[0])
				return "Login Required"
	

		c.title=str(__name__)
		c.subtitle=None
		c.error_message=None
	
		c.show_nav=self.get_session().is_session_created()

		return self.simi_index()

	def simi_index(self):
		raise "Not-Implemented!!!"


	def get_session(self):
		if not self.simi_session:
			self.simi_session=SimiSession(request)
		
		return self.simi_session


	def is_login_required(self):
		return False



class SessionException:
	def __init__(self, value):
		self.value=value

	def __str__(self):
		return repr(self.value)


