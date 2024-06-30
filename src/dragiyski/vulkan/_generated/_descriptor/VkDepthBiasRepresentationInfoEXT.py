from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDepthBiasRepresentationInfoEXT'
_member_list_ = ['sType', 'pNext', 'depthBiasRepresentation', 'depthBiasExact']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEPTH_BIAS_REPRESENTATION_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'depthBiasRepresentation': {
        'type': CIntType('c_int'),
        'type_name': 'VkDepthBiasRepresentationEXT',
        'enum': 'VkDepthBiasRepresentationEXT',
        'is_string': False,
    },
    'depthBiasExact': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDepthBiasInfoEXT',
    'VkPipelineRasterizationStateCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
