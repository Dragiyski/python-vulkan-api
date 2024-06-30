from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceExternalBufferProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalBufferInfo', 'pExternalBufferProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pExternalBufferInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalBufferInfo')),
        'is_string': False,
    },
    'pExternalBufferProperties': {
        'type': CPointerType(CComplexType('VkExternalBufferProperties')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
