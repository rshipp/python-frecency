from __future__ import division
import math

def score_item(recencies, time_constant):
    """Calculates the absolute score.

    :param recencies: an iterable containing time offsets from current
                      time
    :param time_constant: a number that should not be less than or equal
                          to zero, unless you want strange results
    """
    return sum((math.exp(-r / time_constant) for r in recencies))
