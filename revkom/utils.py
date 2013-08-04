"""
Utility functions and classes.
"""

from collections import Iterable, Mapping, deque


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


def flat_list(*args):
    """
    Flattens nested iterables (excluding strings) into a list. Any strings or
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
    # This is the fastest method according to tests run by Peter Bengtsson:
    # http://www.peterbe.com/plog/uniqifiers-benchmark
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]


def unique_string_list(*args):
    """
    Flattens sequences, removing duplicates and non-strings, returning a list.
    """
    return [obj for obj in unique_list(flat_list(*args))
            if isinstance(obj, basestring)]


def unique_callable_list(*args):
    """
    Flattens sequences, removing duplicates and non-strings, returning a list.
    TODO: Write a test
    """
    return [obj for obj in unique_list(flat_list(*args))
            if hasattr(obj, '__call__')]


class EasyList(list):
    """
    A list with utility functions to make it easier to manipulate.
    """

    def insert_before(self, target, *items):
        """
        Insert items before a specified target in the list, in the order in
        which they are passed.
        """
        before_target = self.index(target)
        for item in reversed(items):
            self.insert(before_target, item)

    def insert_after(self, target, *items):
        """
        Insert items after a specified target in the list, in the order in
        which they are passed.
        """
        after_target = self.index(target) + 1
        for item in items:
            self.insert(after_target, item)

    def extend_left(self, iterable):
        """
        Extend list by appending elements from iterable to the left-hand-side
        of the list, preserving their order.
        """
        #new_list = self.__class__(iterable)
        #new_list.extend(self)
        #self = new_list
        for item in reversed(iterable):

    def prepend(self, item):
        """
        Add items to the beginning of the list.
        """
        new_list = self.__class__(items)
        new_list.extend(self)


#class PythonNameList(list):
#    """
#    A flat list of strings representing Python dotted names, or both dotted
#    names and actual objects.
#    """
#    def __init__(self, *args, **kwargs):
#        """
#        """
#        super(PythonNameList, self).__init__()
#        self.only_strings = kwargs.get('only_strings', False)
#        self.uniquify = kwargs.get('uniquify', False)
#        self.extend([obj for obj in self._flatten_fn(*args)
#                    if self.valid_object(obj)])
#
#    @property
#    def _flatten_fn(self):
#        if self.uniquify:
#            return lambda items: unique_list(flat_list(items))
#        return flat_list
#
#    def valid_object(self, obj):
#        if self.allow_strings and isinstance(obj, basestring):
#            return True
#        if self.allow_objects and 
