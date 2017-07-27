import unittest
from scrap.Scrap import Scrap
class TestScrap(unittest.TestCase):
    sc = Scrap('ri7nz')
    def test_init(self):
        self.assertTrue(self.sc)
        self.assertTrue(Scrap(1))
        self.assertTrue(self.sc.getUriList())
    

if __name__ =='__main__':
    unittest.main()
