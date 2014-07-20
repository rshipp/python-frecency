import unittest
import frecency

class TestScoreItem(unittest.TestCase):

    def test_weight_assigned_correctly(self):
        self.assertAlmostEquals(2.955684590875269,
                frecency.score_item([50, 30, 600, 200], 600),
                places=10)
        self.assertAlmostEquals(2.3168950227541245,
                frecency.score_item([50, 30.4, 200], 330),
                places=10)
        self.assertAlmostEquals(0.2865047968601901,
                frecency.score_item([500], 400),
                places=10)

    def test_raises_error_on_invalid_input(self):
        self.assertRaises(TypeError, frecency.score_item, [50, 30], "string")
        self.assertRaises(TypeError, frecency.score_item, 10, 600)
        self.assertRaises(TypeError, frecency.score_item, ["hi"], 600)
        self.assertRaises(TypeError, frecency.score_item, "string", 600)
        self.assertRaises(TypeError, frecency.score_item, "string", "string")
        self.assertRaises(TypeError, frecency.score_item, ["string"], "string")
        self.assertRaises(TypeError, frecency.score_item, [50, 30], None)
        self.assertRaises(TypeError, frecency.score_item, [None], 600)

    def test_empty_list_returns_zero(self):
        self.assertEquals(0, frecency.score_item([], 600))
        self.assertEquals(0, frecency.score_item([], 10.2))
        self.assertEquals(0, frecency.score_item([], 0))
        self.assertEquals(0, frecency.score_item([], -600))

    def test_negative_recency_works(self):
        self.assertAlmostEquals(5.859195364518158,
                frecency.score_item([50,-10,60,200,-500],600),
                places=10)
        self.assertAlmostEquals(6.804121392023058,
                frecency.score_item([-300,12,-72.5,120,-50],300),
                places=10)
        self.assertAlmostEquals(1.9477340410546757,
                frecency.score_item([-200],300),
                places=10)
        self.assertAlmostEquals(6.905469613962053,
                frecency.score_item([-50,-10,-60,-200,-500],600),
                places=10)

    def test_zero_time_constant_raises_exception(self):
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50, 30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50, -30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [-50, 30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [0, 0], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50], 0)


class TestScoreItems(unittest.TestCase):

    def test_correct_order(self):
        pass

    def test_raises_error_on_invalid_input(self):
        pass

    def test_empty_dict_returns_empty_dict(self):
        pass

    def test_empty_recencies_list_returns_zero(self):
        pass
