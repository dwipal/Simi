from simi.tests import *

class TestLogtestController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='logtest'))
        # Test response...
