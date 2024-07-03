from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCreateShadersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'createInfoCount', 'pCreateInfos', 'pAllocator', 'pShaders']
_argument_info_ = {
    'device': {
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
        'type': CPointerType(CComplexType('VkShaderCreateInfoEXT')),
        'is_string': False,
        'length': [['createInfoCount']],
        'output': False,
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
        'output': False,
    },
    'pShaders': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['createInfoCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_INCOMPATIBLE_SHADER_BINARY_EXT', 'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_INITIALIZATION_FAILED'}
