from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueueSubmit2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'submitCount', 'pSubmits', 'fence']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'submitCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pSubmits': {
        'type': CPointerType(CComplexType('VkSubmitInfo2')),
        'is_string': False,
        'length': [['submitCount']],
        'output': False,
    },
    'fence': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST'}
