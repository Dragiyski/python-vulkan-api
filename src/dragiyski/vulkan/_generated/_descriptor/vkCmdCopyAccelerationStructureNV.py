from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdCopyAccelerationStructureNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'dst', 'src', 'mode']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'dst': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'src': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'mode': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
