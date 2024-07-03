import ctypes
from .._view import ArrayView
from collections.abc import Collection, Iterable

def field_access(field_name):
    """Access field of a Structure/Union. Only usable as last call in the chain"""
    def __get__(self):
        return type(self).__base__.__getattribute__(self, field_name)
    
    def __set__(self, value):
        return type(self).__base__.__setattr__(self, field_name, value)
    
    __get__.__qualname__ = f'<{field_access.__name__}>.{__get__.__name__}'
    __set__.__qualname__ = f'<{field_access.__name__}>.{__set__.__name__}'
    
    return __get__, __set__

def property_cache(property_name):
    """Cache the value of a property after transformation. Preferably first in the chain"""
    def chain(get_value, set_value):
        def __get__(self):
            if property_name not in self.__dict__:
                self.__dict__[property_name] = get_value(self)
            return self.__dict__[property_name]
        
        def __set__(self, value):
            self.__dict__.pop(property_name, None)
            set_value(self, value)
            if property_name not in self.__dict__:
                self.__dict__[property_name] = value
    
        __get__.__qualname__ = f'<{property_cache.__name__}>.{__get__.__name__}'
        __set__.__qualname__ = f'<{property_cache.__name__}>.{__set__.__name__}'
        
        return __get__, __set__
    return chain

def auto_string():
    def chain(get_value, set_value):
        def __get__(self):
            value = get_value(self)
            if isinstance(value, bytes):
                value = value.decode()
            return value
        
        def __set__(self, value):
            if isinstance(value, str):
                value = value.encode()
            set_value(self, value)
    
        __get__.__qualname__ = f'<{auto_string.__name__}>.{__get__.__name__}'
        __set__.__qualname__ = f'<{auto_string.__name__}>.{__set__.__name__}'
        
        return __get__, __set__
    return chain

class AutoPointerArrayView(ArrayView):
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

def auto_pointer(value_type):
    def chain(get_value, set_value):
        def __get__(self):
            ptr = get_value(self)
            return ptr.contents if ptr else None
        
        def __set__(self, value):
            if isinstance(value, value_type.get_c_type()):
                value = ctypes.pointer(value)
            set_value(self, value)
    
        __get__.__qualname__ = f'<{auto_pointer.__name__}>.{__get__.__name__}'
        __set__.__qualname__ = f'<{auto_pointer.__name__}>.{__set__.__name__}'

        return __get__, __set__
    return chain

def sparse_array_length_property(item_type, property_name, contigous_field_name, sparse_field_name, get_length, set_length):
    # item_type can be still unresolved during this call, but it will be resolved before structures are first used.
    pointer_wrapper = auto_pointer(item_type)
    def chain(get_item, set_item):
        get_pointer, set_pointer = pointer_wrapper(get_item, set_item)
        def __get__(self):
            ctype = item_type.get_c_type()
            if property_name not in self.__dict__:
                ptr = type(self).__base__.__getattribute__(self, contigous_field_name)
                if ptr:
                    array = ctypes.cast(ptr, ctype * get_length())
                    self.__dict__[property_name] = ArrayView(array, get_item, set_item)
                else:
                    ptr = type(self).__base__.__getattribute__(self, sparse_field_name)
                    if ptr:
                        array = ctypes.cast(ptr, ctypes.POINTER(ctype) * get_length())
                        self.__dict__[property_name] = ArrayView(array, get_pointer, set_pointer)
                    else:
                        self.__dict__[property_name] = None
            return self.__dict__[property_name]
        
        def __set__(self, value):
            ctype = item_type.get_c_type()
            if isinstance(value, ctypes.Array):
                if value._type_ is ctype:
                    type(self).__base__.__setattr__(self, contigous_field_name, ctypes.cast(value, ctypes.POINTER(ctype)))
                    type(self).__base__.__setattr__(self, sparse_field_name, None)
                elif value._type_ is ctypes.POINTER(ctype):
                    type(self).__base__.__setattr__(self, sparse_field_name, ctypes.cast(value, ctypes.POINTER(ctypes.POINTER(ctype))))
                    type(self).__base__.__setattr__(self, contigous_field_name, None)
                else:
                    raise TypeError('Invalid item type for ctypes.Array: expected %r or %r, got %r' % (ctype, ctypes.POINTER(ctype), value._type_))
                self.__dict__[property_name] = value
                length = len(value)
            else:
                if not isinstance(value, Collection):
                    if isinstance(value, Iterable):
                        value = list(value)
                    else:
                        length = len(value)
                        raise TypeError('The provided value is not Iterable or Collection')
                array = ctypes(ctypes.POINTER(ctype) * length)()
                view = ArrayView(array, get_pointer, set_pointer)
                view[:] = value
                type(self).__base__.__setattr__(self, sparse_field_name, ctypes.cast(array, ctypes.POINTER(ctypes.POINTER(ctype))))
                type(self).__base__.__setattr__(self, contigous_field_name, None)
                self.__dict__[property_name] = view
            try:
                set_length(length)
            except Exception:
                self.__dict__.pop(property_name, None)
                raise
    
        __get__.__qualname__ = f'<{sparse_array_length_property.__name__}>.{__get__.__name__}'
        __set__.__qualname__ = f'<{sparse_array_length_property.__name__}>.{__set__.__name__}'

        return __get__, __set__
    return chain

def array_length_property(item_type, property_name, field_name, get_length, set_length):
    def chain(get_item, set_item):
        def __get__(self):
            ctype = item_type.get_c_type()
            if property_name not in self.__dict__:
                ptr = type(self).__base__.__getattribute__(self, field_name)
                if ptr:
                    array = ctypes.cast(ptr, ctype * get_length())
                    self.__dict__[property_name] = ArrayView(array, get_item, set_item)
                else:
                    self.__dict__[property_name] = None
            return self.__dict__[property_name]
        
        def __set__(self, value):
            ctype = item_type.get_c_type()
            if isinstance(value, ctypes.Array):
                if value._type_ is ctype:
                    type(self).__base__.__setattr__(self, field_name, ctypes.cast(value, ctypes.POINTER(ctype)))
                else:
                    raise TypeError('Invalid item type for ctypes.Array: expected %r, got %r' % (ctype, value._type_))
                self.__dict__[property_name] = value
            else:
                if not isinstance(value, Collection):
                    if isinstance(value, Iterable):
                        value = list(value)
                    else:
                        raise TypeError('The provided value is not Iterable or Collection')
                length = len(value)
                array = ctypes(ctype * length)()
                view = ArrayView(array, get_item, set_item)
                view[:] = value
                type(self).__base__.__setattr__(self, field_name, ctypes.cast(array, ctypes.POINTER(ctype)))
                self.__dict__[property_name] = view
            try:
                set_length(length)
            except Exception:
                self.__dict__.pop(property_name, None)
                raise

        __get__.__qualname__ = f'<{sparse_array_length_property.__name__}>.{__get__.__name__}'
        __set__.__qualname__ = f'<{sparse_array_length_property.__name__}>.{__set__.__name__}'

        return __get__, __set__
    return chain
