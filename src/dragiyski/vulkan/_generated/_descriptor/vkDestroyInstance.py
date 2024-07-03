from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkDestroyInstance'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pAllocator']
_argument_info_ = {
    'instance': {
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
