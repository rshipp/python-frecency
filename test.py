import unittest
import frecency

class TestFrecency(unittest.TestCase):

    def test_weight_assigned_correctly(self):
        self.assertAlmostEquals(2.9557,
                frecency.score_item([50,30,600,200],600), 
                delta=0.001)
         
