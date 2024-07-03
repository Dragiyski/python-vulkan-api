from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueueBindSparse'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'bindInfoCount', 'pBindInfo', 'fence']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'bindInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pBindInfo': {
        'type': CPointerType(CComplexType('VkBindSparseInfo')),
        'is_string': False,
        'length': [['bindInfoCount']],
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
