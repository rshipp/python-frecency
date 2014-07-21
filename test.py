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
                frecency.score_item([50, -10, 60, 200, -500], 600),
                places=10)
        self.assertAlmostEquals(6.804121392023058,
                frecency.score_item([-300, 12, -72.5, 120, -50], 300),
                places=10)
        self.assertAlmostEquals(1.9477340410546757,
                frecency.score_item([-200], 300),
                places=10)
        self.assertAlmostEquals(6.905469613962053,
                frecency.score_item([-50, -10, -60, -200, -500], 600),
                places=10)

    def test_zero_time_constant_raises_exception(self):
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50, 30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50, -30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [-50, 30], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [0, 0], 0)
        self.assertRaises(ZeroDivisionError, frecency.score_item, [50], 0)


class TestScoreItems(unittest.TestCase):

    def setUp(self):
        self.input1 = {
            'site1': [50, 30, 600, 200],
            'site2': [500],
            'site3': [50, 30.4, 200],
            'site4': [10, 300, 400, 50, 60],
        }
        self.input2 = {
            2: [50, 3.4, 200],
            1: [10, 30],
        }
        self.input3 = {
            'site2': [100],
        }
        self.output1 = {
            'site4': 3.9283010652321257,
            'site2': 0.4345982085070782,
            'site3': 2.5871712080915095,
            'site1': 2.955684590875269,
        }
        self.output2 = {
            2: 2.630925083807756,
            1: 1.9347008783223316,
        }
        self.output3 = {
            'site2': 0.8464817248906141,
        }


    def test_correct_weights_assigned(self):
        output = frecency.score_items(self.input1, 600)
        for key, value in self.output1.items():
            self.assertAlmostEquals(value, output[key], places=10)
        self.assertEquals(4, len(output))

        output = frecency.score_items(self.input2, 600)
        for key, value in self.output2.items():
            self.assertAlmostEquals(value, output[key], places=10)
        self.assertEquals(2, len(output))

        output = frecency.score_items(self.input3, 600)
        for key, value in self.output3.items():
            self.assertAlmostEquals(value, output[key], places=10)
        self.assertEquals(1, len(output))

    def test_raises_error_on_invalid_input(self):
        pass

    def test_empty_dict_returns_empty_dict(self):
        pass

    def test_empty_recencies_list_returns_zero(self):
        pass
