from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineRasterizationLineStateCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'lineRasterizationMode', 'stippledLineEnable', 'lineStippleFactor', 'lineStipplePattern']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'lineRasterizationMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkLineRasterizationModeKHR',
        'enum': 'VkLineRasterizationModeKHR',
        'is_string': False,
    },
    'stippledLineEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'lineStippleFactor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'lineStipplePattern': {
        'type': CIntType('c_uint16'),
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
