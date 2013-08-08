"""
Utilities for working with collections.
"""

from __future__ import absolute_import
from collections import Iterable, Mapping
from functools import partial
from revkom.mixins import PropMetaclass
#from revkom.utils.klass import boolean_property


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


class EasyList(list):
    """
    A list with utility functions designed to make it easier to manipulate.

    The methods present on Python's built-in ``list()`` reflect its underlying
    data structure, and thus the set of operations that may be performed on
    lists efficiently. The default methods are also atomic (e.g. an insert
    will only take a single item to insert), probably because good Python
    means composing atomic operations with functional operators. EasyList,
    by contrast, is designed for clean and readable code when efficiency is
    not a concern.
    """
    __metaclass__ = PropMetaclass

    def __new__(cls, *args, **kwargs):
        #cls.print_foo()
        return super(EasyList, cls).__new__(cls, *args, **kwargs)

    #def __new__(cls, *args, **kwargs):
    #    instance = super(EasyList, cls).__new__(cls, *args, **kwargs)
    #    instance.add_boolean_prop('flat', False)

    def __init__(self, *iterables, **kwargs):
        super(EasyList, self).__init__()
        map(self.extend, iterables)
        #self.add_boolean_props(['flat', 'unique'], False)
        #self.add_boolean_prop('flat', False)

    #def __getattribute__(self, name):
    #    return object.__getattribute__(self, name)

    ###
    # Custom attributes
    ###
    # TODO: Surely we can abstract away this boilerplate? Something like:
    #boolean_property(self, 'flat', False)
    #flat = boolean_property(False)
    #unique = boolean_property(False)

    #@property
    #def flat(self):
    #    return getattr(self, '_flat', False)

    #@flat.setter
    #def flat(self, truth):
    #    self._flat = bool(truth)

    #@property
    #def unique(self):
    #    return getattr(self, '_unique', False)

    #@unique.setter
    #def unique(self, truth):
    #    self._unique = bool(truth)

    ###
    # Familiar and methods
    ###

    def insert(self, index, *items):
        """
        Insert items into the array, at index, in the order they are passed,
        and return self.
        """
        insert_at_index = partial(super(EasyList, self).insert, index)
        map(insert_at_index, reversed(items))
        #[super(EasyList, self).insert(index, item) for item in reversed(items)]
        return self

    def insert_before(self, target, *items):
        """
        Insert items before a specified target in the list, in the order in
        which they are passed, and return self.
        """
        return self.insert(self.index(target), *items)

    def insert_after(self, target, *items):
        """
        Insert items after a specified target in the list, in the order in
        which they are passed, and return self.
        """
        return self.insert(self.index(target) + 1, *items)

    def extend(self, *iterables):
        map(super(EasyList, self).extend, iterables)
        return self

    def extend_left(self, *iterables):
        """
        Extend list by appending elements from iterables to the left-hand side
        of the list, preserving their order, and return self.
        """
        [self.insert(0, item) for iterable in iterables for item in reversed(iterable)]
        return self

    def prepend(self, *items):
        """
        Add item to the beginning of the list, and return self.
        """
        [self.insert(0, item) for item in items]
        return self

    ###
    # Python magic
    ###
