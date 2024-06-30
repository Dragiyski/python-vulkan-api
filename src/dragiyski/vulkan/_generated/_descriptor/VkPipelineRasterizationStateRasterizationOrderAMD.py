from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationStateRasterizationOrderAMD'
_member_list_ = ['sType', 'pNext', 'rasterizationOrder']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_RASTERIZATION_ORDER_AMD',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'rasterizationOrder': {
        'type': CIntType('c_int'),
        'type_name': 'VkRasterizationOrderAMD',
        'enum': 'VkRasterizationOrderAMD',
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
