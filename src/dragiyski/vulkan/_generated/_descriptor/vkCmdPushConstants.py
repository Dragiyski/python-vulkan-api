from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdPushConstants'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'layout', 'stageFlags', 'offset', 'size', 'pValues']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'size': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pValues': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['size']],
        'output': False,
    },
}
_return_type_ = CVoidType()
