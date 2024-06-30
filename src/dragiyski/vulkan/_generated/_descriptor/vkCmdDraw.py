from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDraw'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'vertexCount', 'instanceCount', 'firstVertex', 'firstInstance']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstVertex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstInstance': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
