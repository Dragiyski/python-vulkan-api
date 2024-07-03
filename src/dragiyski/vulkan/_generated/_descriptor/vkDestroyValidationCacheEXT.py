from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkDestroyValidationCacheEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'validationCache', 'pAllocator']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'validationCache': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
