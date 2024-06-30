from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceSparseImageFormatProperties2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pFormatInfo', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pFormatInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceSparseImageFormatInfo2')),
        'is_string': False,
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkSparseImageFormatProperties2')),
        'is_string': False,
        'length': [['pPropertyCount']],
    },
}
_return_type_ = CVoidType()
