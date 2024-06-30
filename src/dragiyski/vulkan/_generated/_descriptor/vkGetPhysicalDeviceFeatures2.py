from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceFeatures2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pFeatures']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pFeatures': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceFeatures2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
