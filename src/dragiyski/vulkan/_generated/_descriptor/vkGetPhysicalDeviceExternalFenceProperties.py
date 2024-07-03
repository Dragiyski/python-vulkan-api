from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceExternalFenceProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pExternalFenceInfo', 'pExternalFenceProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pExternalFenceInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceExternalFenceInfo')),
        'is_string': False,
        'output': False,
    },
    'pExternalFenceProperties': {
        'type': CPointerType(CComplexType('VkExternalFenceProperties')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
