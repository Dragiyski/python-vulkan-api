from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDispatchBase'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'baseGroupX', 'baseGroupY', 'baseGroupZ', 'groupCountX', 'groupCountY', 'groupCountZ']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'baseGroupX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'baseGroupY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'baseGroupZ': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'groupCountX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'groupCountY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'groupCountZ': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
