from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkDebugMarkerSetObjectNameEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pNameInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pNameInfo': {
        'type': CPointerType(CComplexType('VkDebugMarkerObjectNameInfoEXT')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
