from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdEndTransformFeedbackEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstCounterBuffer', 'counterBufferCount', 'pCounterBuffers', 'pCounterBufferOffsets']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstCounterBuffer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'counterBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCounterBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['counterBufferCount']],
        'output': False,
    },
    'pCounterBufferOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'is_string': False,
        'length': [['counterBufferCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
