import ctypes

class CType(ctypes.Structure):
    pass

from .VkShadingRatePaletteNV import CType as VkShadingRatePaletteNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]

descriptor = {
    'extends': {
        'VkPipelineViewportStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkShadingRatePaletteNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_SHADING_RATE_IMAGE_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shadingRateImageEnable': {'python_name': ['shading', 'rate', 'image', 'enable']},
        'viewportCount': {'python_name': ['viewport', 'count']},
        'pShadingRatePalettes': {'python_name': ['p', 'shading', 'rate', 'palettes'], 'len': [['viewportCount']], 'type': 'VkShadingRatePaletteNV'},
    }
}
