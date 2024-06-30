from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDestroyCudaFunctionNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'function', 'pAllocator']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'function': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
