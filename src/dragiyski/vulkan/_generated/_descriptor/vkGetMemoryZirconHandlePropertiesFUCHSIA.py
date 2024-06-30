from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetMemoryZirconHandlePropertiesFUCHSIA'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'handleType', 'zirconHandle', 'pMemoryZirconHandleProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'zirconHandle': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pMemoryZirconHandleProperties': {
        'type': CPointerType(CComplexType('VkMemoryZirconHandlePropertiesFUCHSIA')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_EXTERNAL_HANDLE'}
