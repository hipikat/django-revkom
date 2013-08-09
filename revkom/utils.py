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
    Flatten nested iterables (excluding strings) into a list. Any strings or
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
    flat = BooleanData(False)
    unique = BooleanData(False)

    def __init__(self, *iterables, **kwargs):
        # Pre- and post-processors are functions that take and return
        # iterables as arguments before and after operations on the list.
        self._preprocessors = []
        self._postprocessors = []
        super(EasyList, self).__init__()
        # Register observers for changes on the list's properties
        self.flat.attach_observer("set_true", self.flatten)
        self.unique.attach_observer("set_true", self.uniquify)
        # Decorate instance methods according to the list's properties
        self._setup_processors()
        # Populate our self with initial data
        items = self._preprocess(iterables)
        map(self.extend, iterables)
        self._postprocess()

    def _setup_processors():
        if self.flat:
            self._preprocessors.append(flat_list)
        if self.unique:
            self._preprocessors.append(self._uniquify)

    def _preprocess(*items):
        for func in self._preprocessors:
            items = func(items)
        return items

    def _postprocess():
        [func() for func in self._postprocessors]

    ###
    # Familiar and methods
    ###

    def insert(self, index, *items):
        """
        Insert items into the array, at index, in the order they are passed,
        and return self.
        """
        for func in self._preprocessors:
            items = func(items)
        insert_at_index = partial(super(EasyList, self).insert, index)
        map(insert_at_index, reversed(items))
        for func in self._postprocessors:
            func()
        return self

    def _insert_before(self, target, *items):
        """
        Insert items before a specified target in the list, in the order in
        which they are passed, and return self.
        """
        return self.insert(self.index(target), *items)

    def _insert_after(self, target, *items):
        """
        Insert items after a specified target in the list, in the order in
        which they are passed, and return self.
        """
        return self.insert(self.index(target) + 1, *items)

    def _extend(self, *iterables):
        map(super(EasyList, self).extend, iterables)
        return self

    def _extend_left(self, *iterables):
        """
        Extend list by appending elements from iterables to the left-hand side
        of the list, preserving their order, and return self.
        """
        [self.insert(0, item) for iterable in iterables for item in reversed(iterable)]
        return self

    def _prepend(self, *items):
        """
        Add item to the beginning of the list, and return self.
        """
        [self.insert(0, item) for item in items]
        return self

    ###
    # Helpers for special properites of the list
    ###

    def flatten(self):
        """
        Flatten nested iterables (excluding strings).
        """
        flat_self = flat_list(self)
        del self[:]
        self.extend(flat_self)

    def uniquify(self):
        """
        Remove duplicate elements from the list (keeping the earliest
        occurences (from left to right)).
        """
        unique_self = unique_list(self)
        del self[:]
        self.extend(unique_self)

    ###
    # Python magic
    ###
