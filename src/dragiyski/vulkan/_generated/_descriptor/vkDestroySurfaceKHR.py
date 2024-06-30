from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDestroySurfaceKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'surface', 'pAllocator']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
