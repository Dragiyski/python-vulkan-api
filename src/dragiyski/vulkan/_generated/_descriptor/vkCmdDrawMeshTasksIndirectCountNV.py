from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDrawMeshTasksIndirectCountNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'buffer', 'offset', 'countBuffer', 'countBufferOffset', 'maxDrawCount', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'countBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'countBufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'maxDrawCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
