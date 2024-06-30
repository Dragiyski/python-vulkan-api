from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationStateStreamCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'rasterizationStream']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_STREAM_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineRasterizationStateStreamCreateFlagsEXT',
        'enum': 'VkPipelineRasterizationStateStreamCreateFlagsEXT',
        'is_string': False,
    },
    'rasterizationStream': {
        'type': CIntType('c_uint32'),
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
