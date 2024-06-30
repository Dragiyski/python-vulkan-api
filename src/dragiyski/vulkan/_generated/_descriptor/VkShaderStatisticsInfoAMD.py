from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShaderStatisticsInfoAMD'
_member_list_ = ['shaderStageMask', 'resourceUsage', 'numPhysicalVgprs', 'numPhysicalSgprs', 'numAvailableVgprs', 'numAvailableSgprs', 'computeWorkGroupSize']
_member_info_ = {
    'shaderStageMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'resourceUsage': {
        'type': CComplexType('VkShaderResourceUsageAMD'),
        'type_name': 'VkShaderResourceUsageAMD',
        'structure': 'VkShaderResourceUsageAMD',
        'is_string': False,
    },
    'numPhysicalVgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'numPhysicalSgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'numAvailableVgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'numAvailableSgprs': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'computeWorkGroupSize': {
        'type': CArrayType(CIntType('c_uint32'), 3),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkShaderResourceUsageAMD',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
