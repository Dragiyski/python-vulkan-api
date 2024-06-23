import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineViewportShadingRateImageStateCreateInfoNV',
    },
    'input_of': {
        'vkCmdSetViewportShadingRatePaletteNV',
    },
    'output_of': set(),
    'member_map': {
        'shadingRatePaletteEntryCount': {'python_name': ['shading', 'rate', 'palette', 'entry', 'count']},
        'pShadingRatePaletteEntries': {'python_name': ['p', 'shading', 'rate', 'palette', 'entries'], 'len': [['shadingRatePaletteEntryCount']], 'type': 'VkShadingRatePaletteEntryNV'},
    }
}
