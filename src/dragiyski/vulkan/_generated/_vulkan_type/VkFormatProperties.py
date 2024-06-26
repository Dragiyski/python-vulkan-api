import ctypes

class VkFormatProperties(ctypes.Structure):
    _fields_ = [
        ('linearTilingFeatures', ctypes.c_uint32),
        ('optimalTilingFeatures', ctypes.c_uint32),
        ('bufferFeatures', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkFormatProperties2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceFormatProperties',
    }
    _python_name_ = {
        'linearTilingFeatures': 'linear_tiling_features',
        'optimalTilingFeatures': 'optimal_tiling_features',
        'bufferFeatures': 'buffer_features',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'linearTilingFeatures': 'VkFormatFeatureFlags',
        'optimalTilingFeatures': 'VkFormatFeatureFlags',
        'bufferFeatures': 'VkFormatFeatureFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkFormatProperties._type_ = {
    'linearTilingFeatures': ctypes.c_uint32,
    'optimalTilingFeatures': ctypes.c_uint32,
    'bufferFeatures': ctypes.c_uint32,
}
