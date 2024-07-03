from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetExecutionGraphPipelineNodeIndexAMDX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'executionGraph', 'pNodeInfo', 'pNodeIndex']
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
    'pNodeInfo': {
        'type': CPointerType(CComplexType('VkPipelineShaderStageNodeCreateInfoAMDX')),
        'is_string': False,
        'output': False,
    },
    'pNodeIndex': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
