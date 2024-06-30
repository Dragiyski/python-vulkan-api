from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSamplerBlockMatchWindowCreateInfoQCOM'
_member_list_ = ['sType', 'pNext', 'windowExtent', 'windowCompareMode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLER_BLOCK_MATCH_WINDOW_CREATE_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'windowExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'windowCompareMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkBlockMatchWindowCompareModeQCOM',
        'enum': 'VkBlockMatchWindowCompareModeQCOM',
        'is_string': False,
    },
}
_extends_ = {
    'VkSamplerCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
