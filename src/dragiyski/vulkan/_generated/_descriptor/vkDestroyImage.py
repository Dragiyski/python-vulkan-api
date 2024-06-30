from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDestroyImage'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pAllocator']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
