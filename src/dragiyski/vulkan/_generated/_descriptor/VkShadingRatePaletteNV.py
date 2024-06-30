from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShadingRatePaletteNV'
_member_list_ = ['shadingRatePaletteEntryCount', 'pShadingRatePaletteEntries']
_member_info_ = {
    'shadingRatePaletteEntryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pShadingRatePaletteEntries': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkShadingRatePaletteEntryNV',
        'enum': 'VkShadingRatePaletteEntryNV',
        'length': [['shadingRatePaletteEntryCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineViewportShadingRateImageStateCreateInfoNV',
}
_input_of_ = {
    'vkCmdSetViewportShadingRatePaletteNV',
}
_output_of_ = set()
