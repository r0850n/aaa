import unittest
from tests import newTest


from common.loadDriver import LoadDriver_realDevice
from tests.newTest import Android_esky_app
 

class SetupTestSuper (unittest.TestCase):
    

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Android_esky_app())
        return suite

 

 

    if __name__ == '__main__':

        runner = unittest.TextTestRunner()

        test_suite = suite()

        runner.run(test_suite)