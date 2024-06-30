from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceToolProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pToolCount', 'pToolProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pToolCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pToolProperties': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceToolProperties')),
        'is_string': False,
        'length': [['pToolCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
