from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceMultisamplePropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'samples', 'pMultisampleProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pMultisampleProperties': {
        'type': CPointerType(CComplexType('VkMultisamplePropertiesEXT')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
