from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRayTracingCaptureReplayShaderGroupHandlesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pipeline', 'firstGroup', 'groupCount', 'dataSize', 'pData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstGroup': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'groupCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['dataSize']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
