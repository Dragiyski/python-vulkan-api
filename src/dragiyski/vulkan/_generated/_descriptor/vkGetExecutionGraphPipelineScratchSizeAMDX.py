from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetExecutionGraphPipelineScratchSizeAMDX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'executionGraph', 'pSizeInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'executionGraph': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSizeInfo': {
        'type': CPointerType(CComplexType('VkExecutionGraphPipelineScratchSizeAMDX')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
