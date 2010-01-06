from simi.lib.base import *
from simibase import *

class LoginController(SimiBaseController):

	def simi_index(self):
		c.title="Welcome to Simi"
		c.subtitle="Please login..."
		

		c.next=request.params.get('next', "albums")

		if request.POST:
			passwd=request.params.get('password', None)
			try:
					self.get_session().create_session(passwd)
					redirect_to(str(c.next))
			except SessionException, e:
					c.error_message="Dah. Please try again."

		self.get_session().delete_session()
		return render('/login.mako')
		
