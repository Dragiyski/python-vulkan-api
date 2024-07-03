from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetAndroidHardwareBufferPropertiesANDROID'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'buffer', 'pProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkAndroidHardwareBufferPropertiesANDROID')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_INVALID_EXTERNAL_HANDLE'}
