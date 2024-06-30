from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkResetCommandBuffer'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'flags']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
