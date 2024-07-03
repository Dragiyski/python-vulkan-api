from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdBindDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'layout', 'firstSet', 'descriptorSetCount', 'pDescriptorSets', 'dynamicOffsetCount', 'pDynamicOffsets']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstSet': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDescriptorSets': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['descriptorSetCount']],
        'output': False,
    },
    'dynamicOffsetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pDynamicOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['dynamicOffsetCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
