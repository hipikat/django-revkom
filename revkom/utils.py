
from collections import Mapping


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
