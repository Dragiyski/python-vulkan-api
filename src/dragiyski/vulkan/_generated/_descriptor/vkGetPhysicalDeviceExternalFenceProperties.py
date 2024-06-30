from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceExternalFenceProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalFenceInfo', 'pExternalFenceProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pExternalFenceInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalFenceInfo')),
        'is_string': False,
    },
    'pExternalFenceProperties': {
        'type': CPointerType(CComplexType('VkExternalFenceProperties')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
