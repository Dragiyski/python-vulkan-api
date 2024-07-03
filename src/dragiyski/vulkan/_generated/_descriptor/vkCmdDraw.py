from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDraw'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'vertexCount', 'instanceCount', 'firstVertex', 'firstInstance']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'vertexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'firstVertex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'firstInstance': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
