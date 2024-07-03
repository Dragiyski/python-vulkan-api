from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceExternalSemaphoreProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalSemaphoreInfo', 'pExternalSemaphoreProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pExternalSemaphoreInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalSemaphoreInfo')),
        'is_string': False,
        'output': False,
    },
    'pExternalSemaphoreProperties': {
        'type': CPointerType(CComplexType('VkExternalSemaphoreProperties')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
