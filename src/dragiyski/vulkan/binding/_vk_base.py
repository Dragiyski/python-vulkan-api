import ctypes

if hasattr(ctypes, 'WINFUNCTYPE'):
    VKAPI_CALL = ctypes.WINFUNCTYPE
    VKAPI_PTR = ctypes.WINFUNCTYPE
else:
    VKAPI_CALL = ctypes.CFUNCTYPE
    VKAPI_PTR = ctypes.CFUNCTYPE

_ptr_print = '0x%016x' if ctypes.sizeof(ctypes.c_void_p) == 8 else '0x%08x'
_nondispatchable_type = ctypes.c_void_p if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint64

def VK_DEFINE_HANDLE(name: str) -> type[ctypes.c_void_p]:
    def handle_repr(self):
        nonlocal name
        if self.value is None:
            return f'{name}(None)'
        return f'%s({_ptr_print})' % (name, self.value)

    return type(name, (ctypes.c_void_p,), {
        '__repr__': handle_repr,
    })

def VK_DEFINE_NON_DISPATCHABLE_HANDLE(name: str) -> type[ctypes.c_uint64|ctypes.c_void_p]:
    def handle_repr(self):
        nonlocal name
        if self.value is None:
            return f'{name}(None)'
        return f'%s({_ptr_print})' % (name, self.value)

    return type(name, (_nondispatchable_type,), {
        '__repr__': handle_repr,
    })
