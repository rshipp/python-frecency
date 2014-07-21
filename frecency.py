from __future__ import division
import math

def score_item(recencies, time_constant):
    """Calculates the absolute score of a given item.

    :param recencies: an iterable containing int time offsets from the current time
    :param time_constant: numeric constant, should be > 0 in most cases
    """
    return sum(math.exp(-r / time_constant) for r in recencies)

def score_items(items, time_constant, score_function=score_item):
    """Calculates the absolute score for all items given.

    :param items: a dictionary of id: recencies pairs
    :param time_constant: numeric constant, should be >0 in most cases
    """
    return {k: score_function(v, time_constant) for k, v in items.items()}
