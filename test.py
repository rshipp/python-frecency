import unittest
import frecency

class TestFrecency(unittest.TestCase):

    def test_weight_assigned_correctly(self):
        self.assertAlmostEquals(2.955684590875269,
                frecency.score_item([50, 30, 600, 200], 600),
                places=10)

    def test_raises_error_on_invalid_input(self):
        self.assertRaises(TypeError, frecency.score_item, [50, 30], "string")
        self.assertRaises(TypeError, frecency.score_item, 10, 600)
        self.assertRaises(TypeError, frecency.score_item, ["hi"], 600)
        self.assertRaises(TypeError, frecency.score_item, "string", 600)
        self.assertRaises(TypeError, frecency.score_item, "string", "string")
        self.assertRaises(TypeError, frecency.score_item, ["string"], "string")

    def test_empty_list_returns_none(self):
        pass

    def test_negative_recency_works(self):
        pass

    def test_zero_time_constant_raises_exception(self):
        pass

