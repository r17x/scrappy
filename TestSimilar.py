from scrap.Similar import Similar as S
import unittest

class TestSimilar(unittest.TestCase):
    similar = S('uxgraph.id')
    def testTo(self):
        s = self.similar
        s.checkUri()
        self.assertIsNone(s.traffic_overiew())

if __name__=='__main__':
    unittest.main()

