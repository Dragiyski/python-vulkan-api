from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkDisplayPowerControlEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'display', 'pDisplayPowerInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDisplayPowerInfo': {
        'type': CPointerType(CComplexType('VkDisplayPowerInfoEXT')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
