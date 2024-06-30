from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineViewportShadingRateImageStateCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'shadingRateImageEnable', 'viewportCount', 'pShadingRatePalettes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'shadingRateImageEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewportCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pShadingRatePalettes': {
        'type': CPointerType(CComplexType('VkShadingRatePaletteNV')),
        'type_name': 'VkShadingRatePaletteNV',
        'structure': 'VkShadingRatePaletteNV',
        'length': [['viewportCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineViewportStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkShadingRatePaletteNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
