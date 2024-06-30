from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetDescriptorBufferOffsetsEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineBindPoint', 'layout', 'firstSet', 'setCount', 'pBufferIndices', 'pOffsets']
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
    'setCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBufferIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'length': [['setCount']],
    },
    'pOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['setCount']],
    },
}
_return_type_ = CVoidType()
