from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdWriteBufferMarker2AMD'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'stage', 'dstBuffer', 'dstOffset', 'marker']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stage': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'marker': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
