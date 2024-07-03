from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkBindBufferMemory2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'bindInfoCount', 'pBindInfos']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'bindInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pBindInfos': {
        'type': CPointerType(CComplexType('VkBindBufferMemoryInfo')),
        'is_string': False,
        'length': [['bindInfoCount']],
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_INVALID_OPAQUE_CAPTURE_ADDRESS'}
