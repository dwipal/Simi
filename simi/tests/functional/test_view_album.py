from simi.tests import *

class TestViewAlbumController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='view_album'))
        # Test response...
