from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationStateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'depthClampEnable', 'rasterizerDiscardEnable', 'polygonMode', 'cullMode', 'frontFace', 'depthBiasEnable', 'depthBiasConstantFactor', 'depthBiasClamp', 'depthBiasSlopeFactor', 'lineWidth']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineRasterizationStateCreateFlags',
        'enum': 'VkPipelineRasterizationStateCreateFlags',
        'is_string': False,
    },
    'depthClampEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'rasterizerDiscardEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'polygonMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkPolygonMode',
        'enum': 'VkPolygonMode',
        'is_string': False,
    },
    'cullMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkCullModeFlags',
        'enum': 'VkCullModeFlags',
        'is_string': False,
    },
    'frontFace': {
        'type': CIntType('c_int'),
        'type_name': 'VkFrontFace',
        'enum': 'VkFrontFace',
        'is_string': False,
    },
    'depthBiasEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depthBiasConstantFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasClamp': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'depthBiasSlopeFactor': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'lineWidth': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDepthBiasRepresentationInfoEXT',
    'VkPipelineRasterizationConservativeStateCreateInfoEXT',
    'VkPipelineRasterizationDepthClipStateCreateInfoEXT',
    'VkPipelineRasterizationLineStateCreateInfoKHR',
    'VkPipelineRasterizationProvokingVertexStateCreateInfoEXT',
    'VkPipelineRasterizationStateRasterizationOrderAMD',
    'VkPipelineRasterizationStateStreamCreateInfoEXT',
}
_includes_ = set()
_included_in_ = {
    'VkGraphicsPipelineCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
