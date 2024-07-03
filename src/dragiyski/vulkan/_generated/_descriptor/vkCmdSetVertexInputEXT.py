from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetVertexInputEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'vertexBindingDescriptionCount', 'pVertexBindingDescriptions', 'vertexAttributeDescriptionCount', 'pVertexAttributeDescriptions']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'vertexBindingDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pVertexBindingDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputBindingDescription2EXT')),
        'is_string': False,
        'length': [['vertexBindingDescriptionCount']],
        'output': False,
    },
    'vertexAttributeDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pVertexAttributeDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputAttributeDescription2EXT')),
        'is_string': False,
        'length': [['vertexAttributeDescriptionCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
