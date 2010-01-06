from simi.tests import *

class TestAlbumsController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='albums'))
        # Test response...
