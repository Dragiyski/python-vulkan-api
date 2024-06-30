from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetShaderInfoAMD'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pipeline', 'shaderStage', 'infoType', 'pInfoSize', 'pInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shaderStage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'infoType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pInfoSize': {
        'type': CPointerType(CIntType('c_size_t')),
        'is_string': False,
    },
    'pInfo': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['pInfoSize']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_FEATURE_NOT_PRESENT', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
