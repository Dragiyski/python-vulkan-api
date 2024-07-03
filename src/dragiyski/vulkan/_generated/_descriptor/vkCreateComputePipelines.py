from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateComputePipelines'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pipelineCache', 'createInfoCount', 'pCreateInfos', 'pAllocator', 'pPipelines']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pipelineCache': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'createInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfos': {
        'type': CPointerType(CComplexType('VkComputePipelineCreateInfo')),
        'is_string': False,
        'length': [['createInfoCount']],
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pPipelines': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['createInfoCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_PIPELINE_COMPILE_REQUIRED'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_INVALID_SHADER_NV', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
