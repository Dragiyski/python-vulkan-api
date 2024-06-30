from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDrawMultiEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'drawCount', 'pVertexInfo', 'instanceCount', 'firstInstance', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drawCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexInfo': {
        'type': CPointerType(CComplexType('VkMultiDrawInfoEXT')),
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
}
_return_type_ = CVoidType()
