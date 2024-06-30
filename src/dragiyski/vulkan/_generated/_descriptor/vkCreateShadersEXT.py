from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCreateShadersEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'createInfoCount', 'pCreateInfos', 'pAllocator', 'pShaders']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'createInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCreateInfos': {
        'type': CPointerType(CComplexType('VkShaderCreateInfoEXT')),
        'is_string': False,
        'length': [['createInfoCount']],
    },
    'pAllocator': {
        'type': CPointerType(CComplexType('VkAllocationCallbacks')),
        'is_string': False,
    },
    'pShaders': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['createInfoCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPATIBLE_SHADER_BINARY_EXT'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
