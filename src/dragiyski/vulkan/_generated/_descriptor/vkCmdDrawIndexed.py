from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDrawIndexed'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'indexCount', 'instanceCount', 'firstIndex', 'vertexOffset', 'firstInstance']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'indexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'firstIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'vertexOffset': {
        'type': CIntType('c_int32'),
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
