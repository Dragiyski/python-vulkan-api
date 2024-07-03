from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPipelinePropertiesEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pPipelineInfo', 'pPipelineProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPipelineInfo': {
        'type': CPointerType(CComplexType('VkPipelineInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pPipelineProperties': {
        'type': CPointerType(CComplexType('VkBaseOutStructure')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
