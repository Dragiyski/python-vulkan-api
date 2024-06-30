from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDestroyDebugReportCallbackEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'callback', 'pAllocator']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'callback': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
