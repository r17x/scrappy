import unittest
from scrap.Scrap import Scrap
class TestScrap(unittest.TestCase):
    sc = Scrap('ri7nz')
    def test_init(self):
        self.assertTrue(self.sc)
        self.assertTrue(Scrap(1))
    def test_uriMethod(self):
        self.assertIsNone(self.sc.getUriList())
    def test_restul(self):
        self.assertIsNotNone(self.sc.uri_list)
    def testStr(self):
        self.assertTrue(self.sc.__str__)
        x = self.sc
#        self.assertTrue(x.getUriList())
        self.assertTrue(x.__str__)

if __name__ =='__main__':
    unittest.main()
