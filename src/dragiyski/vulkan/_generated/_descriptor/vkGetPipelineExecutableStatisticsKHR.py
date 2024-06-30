from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPipelineExecutableStatisticsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pExecutableInfo', 'pStatisticCount', 'pStatistics']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pExecutableInfo': {
        'type': CPointerType(CComplexType('VkPipelineExecutableInfoKHR')),
        'is_string': False,
    },
    'pStatisticCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pStatistics': {
        'type': CPointerType(CComplexType('VkPipelineExecutableStatisticKHR')),
        'is_string': False,
        'length': [['pStatisticCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
