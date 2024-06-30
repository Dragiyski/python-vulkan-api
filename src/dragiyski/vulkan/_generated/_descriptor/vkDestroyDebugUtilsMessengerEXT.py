from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDestroyDebugUtilsMessengerEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'messenger', 'pAllocator']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'messenger': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
