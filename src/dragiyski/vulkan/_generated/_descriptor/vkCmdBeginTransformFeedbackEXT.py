from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdBeginTransformFeedbackEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstCounterBuffer', 'counterBufferCount', 'pCounterBuffers', 'pCounterBufferOffsets']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstCounterBuffer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'counterBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCounterBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['counterBufferCount']],
    },
    'pCounterBufferOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['counterBufferCount']],
    },
}
_return_type_ = CVoidType()
