from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetVertexInputEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'vertexBindingDescriptionCount', 'pVertexBindingDescriptions', 'vertexAttributeDescriptionCount', 'pVertexAttributeDescriptions']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'vertexBindingDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexBindingDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputBindingDescription2EXT')),
        'is_string': False,
        'length': [['vertexBindingDescriptionCount']],
    },
    'vertexAttributeDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexAttributeDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputAttributeDescription2EXT')),
        'is_string': False,
        'length': [['vertexAttributeDescriptionCount']],
    },
}
_return_type_ = CVoidType()
