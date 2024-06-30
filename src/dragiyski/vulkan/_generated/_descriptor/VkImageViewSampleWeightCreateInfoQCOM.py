from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageViewSampleWeightCreateInfoQCOM'
_member_list_ = ['sType', 'pNext', 'filterCenter', 'filterSize', 'numPhases']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_SAMPLE_WEIGHT_CREATE_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'filterCenter': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'filterSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'numPhases': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkImageViewCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkOffset2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
