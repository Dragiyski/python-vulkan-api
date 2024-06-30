from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceQueueFamilyProperties2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pQueueFamilyPropertyCount', 'pQueueFamilyProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pQueueFamilyPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pQueueFamilyProperties': {
        'type': CPointerType(CComplexType('VkQueueFamilyProperties2')),
        'is_string': False,
        'length': [['pQueueFamilyPropertyCount']],
    },
}
_return_type_ = CVoidType()
