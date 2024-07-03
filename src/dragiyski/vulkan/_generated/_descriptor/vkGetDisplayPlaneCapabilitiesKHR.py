from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDisplayPlaneCapabilitiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'mode', 'planeIndex', 'pCapabilities']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'mode': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'planeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCapabilities': {
        'type': CPointerType(CComplexType('VkDisplayPlaneCapabilitiesKHR')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
