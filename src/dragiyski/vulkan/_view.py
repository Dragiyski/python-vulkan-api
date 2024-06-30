import ctypes, weakref

_array_view = weakref.WeakKeyDictionary()

class ArrayView:
    __slots__ = ('__weakref__')

    def __init__(self, target, *, view: callable = lambda v: v):
        _array_view[self] = (target, view)
    
    def __getitem__(self, key):
        target, view = _array_view[self]
        if isinstance(key, int):
            return self.__view(self.__target[key])
        if isinstance(key, slice):
            return list(self.__view(item) for item in self.__target[key])
        raise KeyError(key)
    
    def __len__(self):
        return len(self.__target)
    
    def __iter__(self):
        yield from self.__target
