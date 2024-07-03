from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceQueueFamilyProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pQueueFamilyPropertyCount', 'pQueueFamilyProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pQueueFamilyPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pQueueFamilyProperties': {
        'type': CPointerType(CComplexType('VkQueueFamilyProperties')),
        'is_string': False,
        'length': [['pQueueFamilyPropertyCount']],
        'output': True,
    },
}
_return_type_ = CVoidType()
