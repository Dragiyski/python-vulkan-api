from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceExternalSemaphoreProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalSemaphoreInfo', 'pExternalSemaphoreProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pExternalSemaphoreInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalSemaphoreInfo')),
        'is_string': False,
    },
    'pExternalSemaphoreProperties': {
        'type': CPointerType(CComplexType('VkExternalSemaphoreProperties')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
