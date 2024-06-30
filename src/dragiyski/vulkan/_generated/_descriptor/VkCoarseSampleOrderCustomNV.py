from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCoarseSampleOrderCustomNV'
_member_list_ = ['shadingRate', 'sampleCount', 'sampleLocationCount', 'pSampleLocations']
_member_info_ = {
    'shadingRate': {
        'type': CIntType('c_int'),
        'type_name': 'VkShadingRatePaletteEntryNV',
        'enum': 'VkShadingRatePaletteEntryNV',
        'is_string': False,
    },
    'sampleCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sampleLocationCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSampleLocations': {
        'type': CPointerType(CComplexType('VkCoarseSampleLocationNV')),
        'type_name': 'VkCoarseSampleLocationNV',
        'structure': 'VkCoarseSampleLocationNV',
        'length': [['sampleLocationCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkCoarseSampleLocationNV',
}
_included_in_ = {
    'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
}
_input_of_ = {
    'vkCmdSetCoarseSampleOrderNV',
}
_output_of_ = set()
