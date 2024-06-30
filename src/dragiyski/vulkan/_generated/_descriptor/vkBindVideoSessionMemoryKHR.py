from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkBindVideoSessionMemoryKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'videoSession', 'bindSessionMemoryInfoCount', 'pBindSessionMemoryInfos']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoSession': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bindSessionMemoryInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBindSessionMemoryInfos': {
        'type': CPointerType(CComplexType('VkBindVideoSessionMemoryInfoKHR')),
        'is_string': False,
        'length': [['bindSessionMemoryInfoCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
