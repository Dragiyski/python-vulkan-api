from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDrawMeshTasksIndirectCountEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'buffer', 'offset', 'countBuffer', 'countBufferOffset', 'maxDrawCount', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'countBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'countBufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxDrawCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
