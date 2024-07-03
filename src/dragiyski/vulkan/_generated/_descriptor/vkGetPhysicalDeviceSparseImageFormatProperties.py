from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceSparseImageFormatProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'type', 'samples', 'usage', 'tiling', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkSparseImageFormatProperties')),
        'is_string': False,
        'length': [['pPropertyCount']],
        'output': True,
    },
}
_return_type_ = CVoidType()
