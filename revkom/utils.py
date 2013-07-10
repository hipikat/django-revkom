
from collections import Iterable, Mapping
#from functools import partial


#class RevkomList(list):
#    """
#    A list with utility functions for inserting elements relative to existing
#    elements in the list
#    """
#    def insert_after(target, item, fail_if_missing=True):
#        raise NotImplementedError
#
#    def insert_before(target, item, fail_if_missing=True):
#        raise NotImplementedError


#class FlatList(list):
#    """
#    A flat list - any attempts to insert iterables (with the exception of
#    strings) will result in those iterables being flattened before being
#    inserted into the list.
#    """
#    def __init__(*args, **kwargs):
#        self.append(flat_list(args))
#
#    # TODO: Overload other methods that let items get into lists...


#def method_on_mappings(method_name, mappings, *args):
#    """
#    Call method_name on each mapping in mappings, with args as arguments.
#    """
#    return [getattr(mapping, method_name)(*args) for mapping in mappings]

#def setdefault_on_mappings(mappings, *args):


#setdefault_on_mappings = partial(method_on_mappings, 'setdefault')

#setdefault_on_dicts = partial


#def setdefault_or_get(mapping, key, val):
#    """
#    Convenience for calling setdefault on a mapping, with either one value or
#    a tuple of values passed as arguments.
#    """
#    if len(vals) == 1:
#        mapping.setdefault(key, vals[0])
#    elif len(vals):
#        mapping.setdefault(key, vals)
#    else:
#        mapping.get(key)


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
