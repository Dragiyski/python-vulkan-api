from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetMemoryRemoteAddressNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pMemoryGetRemoteAddressInfo', 'pAddress']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryGetRemoteAddressInfo': {
        'type': CPointerType(CComplexType('VkMemoryGetRemoteAddressInfoNV')),
        'is_string': False,
    },
    'pAddress': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_EXTERNAL_HANDLE'}
