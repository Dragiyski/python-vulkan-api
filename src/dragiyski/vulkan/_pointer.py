import ctypes
import threading
import weakref
import functools

_ptr_ref = weakref.WeakValueDictionary()
_ptr_finalizer = weakref.WeakKeyDictionary()
_pointer_lock = threading.RLock()


class FinalizerAlreadyRegisteredError(RuntimeError):
    pass


def noop(*args, **kwargs):
    pass

def finalize(ptr, obj, callback, /, *args, **kwargs):
    global _pointer_lock, _pointer_storage
    if isinstance(ptr, ctypes._SimpleCData):
        ptr = ptr.value
    if ptr is None:
        return
    if not isinstance(ptr, int) or ptr < 0:
            raise TypeError('Invalid pointer: %r' % ptr)
    if ptr == 0:
        return
    with _pointer_lock:
        if ptr in _ptr_ref:
            if _ptr_ref[ptr] is not obj:
                raise ReferenceError('Cannot associate pointer 0x%016x: %r is different from the already associated %r' % (ptr, obj, _ptr_ref[ptr]))
        _ptr_ref[ptr] = obj
        if callback is not None:
            if obj not in _ptr_finalizer or not _ptr_finalizer[obj].alive:
                _ptr_finalizer[obj] = weakref.finalize(obj, callback, *args, **kwargs)
                return _ptr_finalizer[obj]
            raise FinalizerAlreadyRegisteredError('Finalizer for the given object is already registered')


class PointerStorageType(type):
    def __call__(self, ptr, /, *args, **kwargs):
        global _pointer_lock, _pointer_storage
        if isinstance(ptr, ctypes._SimpleCData):
            ptr = ptr.value
        if ptr is None:
            return
        if not isinstance(ptr, int) or ptr < 0:
            raise TypeError('Invalid pointer: %r' % ptr)
        if ptr == 0:
            return
        with _pointer_lock:
            obj = _ptr_ref.get(ptr, None)
            if obj is not None:
                if not isinstance(obj, self):
                    raise TypeError('Invalid pointer: pointer 0x%016x of type %r, cannot be wrapped into %r' % (ptr, type(obj), self))
                return obj
            obj = object.__new__(self)
            object.__setattr__(obj, '_as_parameter_', ptr)
            _ptr_ref[ptr] = obj
        obj.__init__(*args, **kwargs)
        return obj
