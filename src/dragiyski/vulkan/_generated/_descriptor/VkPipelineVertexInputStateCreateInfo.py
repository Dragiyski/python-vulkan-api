from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineVertexInputStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'vertexBindingDescriptionCount', 'pVertexBindingDescriptions', 'vertexAttributeDescriptionCount', 'pVertexAttributeDescriptions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineVertexInputStateCreateFlags',
        'enum': 'VkPipelineVertexInputStateCreateFlags',
        'is_string': False,
    },
    'vertexBindingDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexBindingDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputBindingDescription')),
        'type_name': 'VkVertexInputBindingDescription',
        'structure': 'VkVertexInputBindingDescription',
        'length': [['vertexBindingDescriptionCount']],
        'is_string': False,
    },
    'vertexAttributeDescriptionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pVertexAttributeDescriptions': {
        'type': CPointerType(CComplexType('VkVertexInputAttributeDescription')),
        'type_name': 'VkVertexInputAttributeDescription',
        'structure': 'VkVertexInputAttributeDescription',
        'length': [['vertexAttributeDescriptionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineVertexInputDivisorStateCreateInfoKHR',
}
_includes_ = {
    'VkVertexInputAttributeDescription',
    'VkVertexInputBindingDescription',
}
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
    'VkGraphicsShaderGroupCreateInfoNV',
}
_input_of_ = set()
_output_of_ = set()
