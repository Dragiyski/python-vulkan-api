import ctypes

class VkDrmFormatModifierProperties2EXT(ctypes.Structure):
    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDrmFormatModifierPropertiesList2EXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'drmFormatModifier': 'drm_format_modifier',
        'drmFormatModifierPlaneCount': 'drm_format_modifier_plane_count',
        'drmFormatModifierTilingFeatures': 'drm_format_modifier_tiling_features',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_drm_format_modifier',
    }
    _vk_enum_ = {
        'drmFormatModifierTilingFeatures': 'VkFormatFeatureFlags2',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDrmFormatModifierProperties2EXT._type_ = {
    'drmFormatModifier': ctypes.c_uint64,
    'drmFormatModifierPlaneCount': ctypes.c_uint32,
    'drmFormatModifierTilingFeatures': ctypes.c_uint64,
}
