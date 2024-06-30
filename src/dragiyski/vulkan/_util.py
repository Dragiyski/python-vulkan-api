import ctypes
import weakref
import re
from threading import RLock
from typing import Iterable


def make_array_ptr_from_iterable(ctype, iterable: Iterable):
    iterable = list(iterable)
    count = len(iterable)
    if count <= 0:
        return None
    array = (ctype * count)()
    for i in range(count):
        array[i] = iterable[i]
    return ctypes.cast(array, ctypes.POINTER(ctype))

def make_c_string_list(iterable: Iterable):
    return list(s.encode() if isinstance(s, str) else s for s in iterable)

def make_python_name(name, *, p = False, s = True):
        words = name.split('_')
        words = [re.findall(r'(?:[A-Z][A-Z0-9]*|^)[a-z0-9]*', word) for word in words]
        words = [word.lower() for x in words for word in x]
        if p and len(words) > 1 and re.fullmatch(r'p+', words[0]):
            words = words[1:]
        elif s and len(words) > 1 and re.fullmatch(r's+', words[0]):
            words = words[1:]
        return '_'.join(words)

def create_handle_storage_meta(binding_type, handle_map):
    def handle_meta_call(self, value):
        if isinstance(value, binding_type):
            value = value.value
        if value in handle_map:
            return handle_map[value]
        raise ReferenceError('No ownership of %s found for: %r' % (self.__name__, value))

    return type(
        'HandleStorageMeta', (type(binding_type),), {
            '__call__': handle_meta_call
        }
    )


class DictionaryNode:
    def __init__(self, parent_node: 'dict | DictionaryNode' = dict()):
        self.__parent_node = parent_node
        self.__this_node = dict()

    def __getitem__(self, key):
        try:
            return self.__this_node[key]
        except KeyError:
            return self.__parent_node[key]

    def __setitem__(self, key, value):
        self.__this_node[key] = value

    def __delitem__(self, key):
        if key in self.__this_node:
            del self.__this_node[key]

    def __iter__(self):
        yield from self.__this_node
        yield from self.__parent_node

    def __len__(self):
        return len(self.__this_node) + len(self.__parent_node)

    def __reversed__(self):
        yield from reversed(self.__parent_node)
        yield from reversed(self.__this_node)

    def __contains__(self, item):
        return item in self.__this_node or item in self.__parent_node

    def keys(self):
        yield from self.__this_node.keys()
        yield from self.__parent_node.keys()

    def values(self):
        yield from self.__this_node.values()
        yield from self.__parent_node.values()

    def items(self):
        yield from self.__this_node.items()
        yield from self.__parent_node.items()

    def own_keys(self):
        yield from self.__this_node.keys()

    def own_values(self):
        yield from self.__this_node.values()

    def own_items(self):
        yield from self.__this_node.items()

    def clear(self):
        self.__this_node.clear()


def noop(*args, **kwargs):
    pass


class noop_finalize:
    def __init__(self, object):
        self.__lock = RLock()
        self.__object = weakref.ref(object, self.__call__)
        self.atexit = False

    def __call__(self):
        with self.__lock:
            self.__object = None

    def alive(self):
        with self.__lock:
            return self.__object is not None

    def peek(self):
        with self.__lock:
            if self.__object is not None:
                object = self.__object()
                if object is not None:
                    return (object, noop, (), {})
            return None

    def detach(self):
        with self.__lock:
            if self.__object is not None:
                object = self.__object()
                self.__object = None
                if object is not None:
                    return (object, noop, (), {})
            return None
