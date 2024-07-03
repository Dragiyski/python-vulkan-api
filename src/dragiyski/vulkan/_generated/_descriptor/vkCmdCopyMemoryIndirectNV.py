from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyMemoryIndirectNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'copyBufferAddress', 'copyCount', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'copyBufferAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'copyCount': {
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
