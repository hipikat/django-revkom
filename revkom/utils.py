"""
Utility functions and classes.
"""

from collections import Iterable, Mapping


def flat_list(*args):
    """
    Flattens nested iterables, excluding strings, into a list. Any strings or
    non-iterable items passed as arguments are just added to the list in the
    order in which they are passed.
    """
    flattened_list = []
    for arg in args:
        if isinstance(arg, Iterable) and not isinstance(arg, basestring):
            flattened_list += flat_list(*arg)
        else:
            flattened_list.append(arg)
    return flattened_list


def unique_list(seq):
    """
    Take a sequence and return a list of unique items from that sequence. The
    order of the original sequence will be preserved, with the first occurence
    of any duplicate items retained and the rest omitted.
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]


def deep_update(mapping, updated):
    """
    Deep, non-destructive updating for dictionaries.
    """
    for (key, val) in updated.iteritems():
        if isinstance(val, Mapping):
            mapping[key] = deep_update(mapping.get(key, {}), val)
        else:
            mapping[key] = updated[key]
    return mapping
