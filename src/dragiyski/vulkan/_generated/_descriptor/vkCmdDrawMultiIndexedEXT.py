from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDrawMultiIndexedEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'drawCount', 'pIndexInfo', 'instanceCount', 'firstInstance', 'stride', 'pVertexOffset']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drawCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pIndexInfo': {
        'type': CPointerType(CComplexType('VkMultiDrawIndexedInfoEXT')),
        'is_string': False,
        'length': [['drawCount']],
    },
    'instanceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'firstInstance': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexOffset': {
        'type': CPointerType(CIntType('c_int32')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
