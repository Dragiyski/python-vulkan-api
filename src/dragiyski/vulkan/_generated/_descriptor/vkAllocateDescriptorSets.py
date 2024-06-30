from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkAllocateDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pAllocateInfo', 'pDescriptorSets']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAllocateInfo': {
        'type': CPointerType(CComplexType('VkDescriptorSetAllocateInfo')),
        'is_string': False,
    },
    'pDescriptorSets': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['pAllocateInfo', 'descriptorSetCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_POOL_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FRAGMENTED_POOL'}
