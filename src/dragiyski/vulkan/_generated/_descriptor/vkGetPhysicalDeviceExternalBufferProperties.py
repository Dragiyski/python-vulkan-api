from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceExternalBufferProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalBufferInfo', 'pExternalBufferProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pExternalBufferInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalBufferInfo')),
        'is_string': False,
        'output': False,
    },
    'pExternalBufferProperties': {
        'type': CPointerType(CComplexType('VkExternalBufferProperties')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
