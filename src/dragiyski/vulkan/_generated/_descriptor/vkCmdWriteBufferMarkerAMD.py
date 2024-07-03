from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdWriteBufferMarkerAMD'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'pipelineStage', 'dstBuffer', 'dstOffset', 'marker']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pipelineStage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'dstOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'marker': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
