from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetCalibratedTimestampsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'timestampCount', 'pTimestampInfos', 'pTimestamps', 'pMaxDeviation']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'timestampCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pTimestampInfos': {
        'type': CPointerType(CComplexType('VkCalibratedTimestampInfoKHR')),
        'is_string': False,
        'length': [['timestampCount']],
    },
    'pTimestamps': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['timestampCount']],
    },
    'pMaxDeviation': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
