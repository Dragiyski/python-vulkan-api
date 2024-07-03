from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDrawMultiEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'drawCount', 'pVertexInfo', 'instanceCount', 'firstInstance', 'stride']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'drawCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pVertexInfo': {
        'type': CPointerType(CComplexType('VkMultiDrawInfoEXT')),
        'is_string': False,
        'length': [['drawCount']],
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
    'stride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
