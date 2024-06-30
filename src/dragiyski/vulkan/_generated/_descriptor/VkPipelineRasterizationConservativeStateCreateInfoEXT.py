from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationConservativeStateCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'conservativeRasterizationMode', 'extraPrimitiveOverestimationSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_CONSERVATIVE_STATE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineRasterizationConservativeStateCreateFlagsEXT',
        'enum': 'VkPipelineRasterizationConservativeStateCreateFlagsEXT',
        'is_string': False,
    },
    'conservativeRasterizationMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkConservativeRasterizationModeEXT',
        'enum': 'VkConservativeRasterizationModeEXT',
        'is_string': False,
    },
    'extraPrimitiveOverestimationSize': {
        'type': CFloatType('c_float'),
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
