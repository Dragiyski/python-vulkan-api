from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkEndCommandBuffer'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_VIDEO_STD_PARAMETERS_KHR', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
