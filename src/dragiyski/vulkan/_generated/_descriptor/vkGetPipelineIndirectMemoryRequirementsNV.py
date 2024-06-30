from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPipelineIndirectMemoryRequirementsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkComputePipelineCreateInfo')),
        'is_string': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
