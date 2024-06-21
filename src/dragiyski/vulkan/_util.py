import ctypes
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

def create_handle_storage_meta(binding_type, handle_map):
    def handle_meta_call(self, value):
        if isinstance(value, binding_type):
            value = value.value
        if value in handle_map:
            return handle_map[value]
        raise ReferenceError('No ownership of %s found for: %r' % (self.__name__, value))
    
    return type('HandleStorageMeta', (type(binding_type),), {
        '__call__': handle_meta_call
    })
