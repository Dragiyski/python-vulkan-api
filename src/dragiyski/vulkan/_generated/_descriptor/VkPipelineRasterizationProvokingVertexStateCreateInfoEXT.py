from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationProvokingVertexStateCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'provokingVertexMode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_PROVOKING_VERTEX_STATE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'provokingVertexMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkProvokingVertexModeEXT',
        'enum': 'VkProvokingVertexModeEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineRasterizationStateCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
