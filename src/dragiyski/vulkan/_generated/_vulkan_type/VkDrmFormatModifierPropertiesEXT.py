import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDrmFormatModifierPropertiesListEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'drmFormatModifier': {'python_name': ['drm', 'format', 'modifier']},
        'drmFormatModifierPlaneCount': {'python_name': ['drm', 'format', 'modifier', 'plane', 'count']},
        'drmFormatModifierTilingFeatures': {'python_name': ['drm', 'format', 'modifier', 'tiling', 'features'], 'type': 'VkFormatFeatureFlags'},
    }
}
