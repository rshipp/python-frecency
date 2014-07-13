from __future__ import division
import math

def score_item(recencies, time_constant):
    """Calculates the absolute score of a given item.

    :param recencies: an iterable containing int time offsets from the current time
    :param time_constant: numeric constant, should be > 0 in most cases
    """
    return sum(math.exp(-r / time_constant) for r in recencies)
