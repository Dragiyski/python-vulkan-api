from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdPushConstants'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'layout', 'stageFlags', 'offset', 'size', 'pValues']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pValues': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'length': [['size']],
    },
}
_return_type_ = CVoidType()
