import ctypes
from typing import Iterable


def make_array_ptr_from_iterable(ctype, iterable: Iterable):
    iterable = list(iterable)
    count = len(iterable)
    if count <= 0:
        return None
    array = ctypes.ARRAY(ctype, count)()
    for i in range(count):
        array[i] = iterable[i]
    return ctypes.cast(array, ctypes.POINTER(ctype))
