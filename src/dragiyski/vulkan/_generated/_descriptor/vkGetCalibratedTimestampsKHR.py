from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetCalibratedTimestampsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'timestampCount', 'pTimestampInfos', 'pTimestamps', 'pMaxDeviation']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'timestampCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pTimestampInfos': {
        'type': CPointerType(CComplexType('VkCalibratedTimestampInfoKHR')),
        'is_string': False,
        'length': [['timestampCount']],
        'output': False,
    },
    'pTimestamps': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['timestampCount']],
        'output': True,
    },
    'pMaxDeviation': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
