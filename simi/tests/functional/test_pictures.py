from simi.tests import *

class TestPicturesController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='pictures'))
        # Test response...
