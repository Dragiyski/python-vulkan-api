from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceProperties')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
