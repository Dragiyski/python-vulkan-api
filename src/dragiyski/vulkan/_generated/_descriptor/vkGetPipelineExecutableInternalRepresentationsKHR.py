from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPipelineExecutableInternalRepresentationsKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pExecutableInfo', 'pInternalRepresentationCount', 'pInternalRepresentations']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pExecutableInfo': {
        'type': CPointerType(CComplexType('VkPipelineExecutableInfoKHR')),
        'is_string': False,
    },
    'pInternalRepresentationCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pInternalRepresentations': {
        'type': CPointerType(CComplexType('VkPipelineExecutableInternalRepresentationKHR')),
        'is_string': False,
        'length': [['pInternalRepresentationCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
