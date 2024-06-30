from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassFragmentDensityMapOffsetEndInfoQCOM'
_member_list_ = ['sType', 'pNext', 'fragmentDensityOffsetCount', 'pFragmentDensityOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBPASS_FRAGMENT_DENSITY_MAP_OFFSET_END_INFO_QCOM',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fragmentDensityOffsetCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pFragmentDensityOffsets': {
        'type': CPointerType(CComplexType('VkOffset2D')),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'length': [['fragmentDensityOffsetCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkSubpassEndInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkOffset2D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
