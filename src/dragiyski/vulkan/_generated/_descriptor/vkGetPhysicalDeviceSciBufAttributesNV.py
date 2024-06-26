from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceSciBufAttributesNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pAttributes']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAttributes': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
