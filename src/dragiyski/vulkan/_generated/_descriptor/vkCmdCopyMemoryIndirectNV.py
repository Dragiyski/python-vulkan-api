from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyMemoryIndirectNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'copyBufferAddress', 'copyCount', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'copyBufferAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'copyCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
