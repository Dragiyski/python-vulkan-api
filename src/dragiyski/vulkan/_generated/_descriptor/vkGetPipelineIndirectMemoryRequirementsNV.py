from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPipelineIndirectMemoryRequirementsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pCreateInfo', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pCreateInfo': {
        'type': CPointerType(CComplexType('VkComputePipelineCreateInfo')),
        'is_string': False,
        'output': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements2')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
