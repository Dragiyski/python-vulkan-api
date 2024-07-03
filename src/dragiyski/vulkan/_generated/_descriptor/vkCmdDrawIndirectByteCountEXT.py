from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDrawIndirectByteCountEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'instanceCount', 'firstInstance', 'counterBuffer', 'counterBufferOffset', 'counterOffset', 'vertexStride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'firstInstance': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'counterBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'counterBufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'counterOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'vertexStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
