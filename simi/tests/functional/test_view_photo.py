from simi.tests import *

class TestViewPhotoController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='view_photo'))
        # Test response...
