from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBindDescriptorSets'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'layout', 'firstSet', 'descriptorSetCount', 'pDescriptorSets', 'dynamicOffsetCount', 'pDynamicOffsets']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstSet': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'descriptorSetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorSets': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['descriptorSetCount']],
    },
    'dynamicOffsetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDynamicOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['dynamicOffsetCount']],
    },
}
_return_type_ = CVoidType()
