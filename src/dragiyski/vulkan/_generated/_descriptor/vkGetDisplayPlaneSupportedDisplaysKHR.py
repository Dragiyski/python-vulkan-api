from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDisplayPlaneSupportedDisplaysKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'planeIndex', 'pDisplayCount', 'pDisplays']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'planeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDisplayCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pDisplays': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['pDisplayCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
