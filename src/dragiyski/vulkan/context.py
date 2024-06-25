import ctypes
from typing import Optional
from threading import RLock
from ._util import DictionaryNode


class Context:
    def __init__(self, parent_context: 'Optional[Context]' = None, ptr = None):
        self._parent = parent_context
        self._map = dict()
        self._lock = RLock()
        self._ptr = ptr

    def get(self, ptr, cls: type = None):
        if isinstance(ptr, ctypes._SimpleCData):
            ptr = ptr.value
        if not isinstance(ptr, int):
            raise TypeError('Invalid pointer: expected instance of %r, got instance of %r' % (int, type(ptr)))
        with self._lock:
            if ptr in self._map:
                finalizer = self._map[ptr]
                maybe_object = finalizer.peek()
                if maybe_object is None:
                    del self._map[ptr]
                    return None
                if cls is not None:
                    if not isinstance(maybe_object[0], cls):
                        raise TypeError('Invalid pointer: expected pointer to %r, got a pointer to %r' % (cls, type(maybe_object[0])))
                return maybe_object[0]
            return None

    def assign(self, ptr, finalizer):
        if isinstance(ptr, ctypes._SimpleCData):
            ptr = ptr.value
        assert isinstance(ptr, int)
        with self._lock:
            self._map[ptr] = finalizer

    def clear(self):
        with self._lock:
            finalizer_list = list(self._map.values())
            for finalizer in finalizer_list:
                finalizer()
            self._map.clear()
        if self._parent is not None:
            self._parent.notify(self._ptr)

    def notify(self, ptr):
        if ptr is None:
            return
        with self._lock:
            if ptr in self._map and not self._map[ptr].alive:
                del self._map[ptr]

    def __enter__(self):
        self._lock.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._lock.__exit__(exc_type, exc_val, exc_tb)
