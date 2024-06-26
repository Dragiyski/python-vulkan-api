import ctypes

class VkFormatProperties3(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearTilingFeatures', ctypes.c_uint64),
        ('optimalTilingFeatures', ctypes.c_uint64),
        ('bufferFeatures', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = {
        'VkFormatProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'linearTilingFeatures': 'linear_tiling_features',
        'optimalTilingFeatures': 'optimal_tiling_features',
        'bufferFeatures': 'buffer_features',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'linearTilingFeatures': 'VkFormatFeatureFlags2',
        'optimalTilingFeatures': 'VkFormatFeatureFlags2',
        'bufferFeatures': 'VkFormatFeatureFlags2',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_3'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_3
        for function in self._init_:
            function(self, *args, **kwargs)

VkFormatProperties3._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'linearTilingFeatures': ctypes.c_uint64,
    'optimalTilingFeatures': ctypes.c_uint64,
    'bufferFeatures': ctypes.c_uint64,
}
