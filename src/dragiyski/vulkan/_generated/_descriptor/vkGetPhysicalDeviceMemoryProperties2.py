from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceMemoryProperties2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pMemoryProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceMemoryProperties2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
