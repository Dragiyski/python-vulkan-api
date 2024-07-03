from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceFeatures'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pFeatures']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pFeatures': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceFeatures')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
