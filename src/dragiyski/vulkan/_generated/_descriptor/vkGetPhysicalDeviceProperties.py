from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceProperties')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
