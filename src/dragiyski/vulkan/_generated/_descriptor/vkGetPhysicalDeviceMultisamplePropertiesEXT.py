from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceMultisamplePropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'samples', 'pMultisampleProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMultisampleProperties': {
        'type': CPointerType(CComplexType('VkMultisamplePropertiesEXT')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
