from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPipelineExecutablePropertiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pPipelineInfo', 'pExecutableCount', 'pProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPipelineInfo': {
        'type': CPointerType(CComplexType('VkPipelineInfoKHR')),
        'is_string': False,
    },
    'pExecutableCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkPipelineExecutablePropertiesKHR')),
        'is_string': False,
        'length': [['pExecutableCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
