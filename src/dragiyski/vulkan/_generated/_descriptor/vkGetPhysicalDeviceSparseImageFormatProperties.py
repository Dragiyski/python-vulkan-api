from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceSparseImageFormatProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'type', 'samples', 'usage', 'tiling', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkSparseImageFormatProperties')),
        'is_string': False,
        'length': [['pPropertyCount']],
    },
}
_return_type_ = CVoidType()
