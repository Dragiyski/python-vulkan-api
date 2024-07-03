from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDecompressMemoryIndirectCountNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'indirectCommandsAddress', 'indirectCommandsCountAddress', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'indirectCommandsAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'indirectCommandsCountAddress': {
        'type': CIntType('c_uint64'),
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
