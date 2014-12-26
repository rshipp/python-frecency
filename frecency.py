from __future__ import division
import math

def score_item(recencies, time_constant):
    """Calculates the absolute score of a given item.

    :param recencies: an iterable containing int time offsets from the current time
    :param time_constant: numeric constant, should be > 0 in most cases
    """
    return sum(math.exp(-r / time_constant) for r in recencies)

def score_items(items, time_constant, score_function=None):
    """Calculates the absolute score for all items given.

    :param items: a dictionary of {id: recencies}, or a list of pairs
    :param time_constant: numeric constant, should be >0 in most cases
    :param score_function: function matching the signature of
                           score_item used to score individual items
    """
    try:
        tuples = items.items()
    except AttributeError:
        tuples = items
    return {k: (score_function or score_item)(v, time_constant) for k, v in tuples}
