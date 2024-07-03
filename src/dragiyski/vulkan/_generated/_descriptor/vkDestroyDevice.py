from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkDestroyDevice'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pAllocator']
_argument_info_ = {
    'device': {
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
