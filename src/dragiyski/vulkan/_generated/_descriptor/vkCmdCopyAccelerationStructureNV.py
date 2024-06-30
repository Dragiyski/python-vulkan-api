from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdCopyAccelerationStructureNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'dst', 'src', 'mode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dst': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'src': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
