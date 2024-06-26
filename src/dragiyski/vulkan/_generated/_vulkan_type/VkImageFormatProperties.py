import ctypes

class VkImageFormatProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
    }
    _included_in_ = {
        'VkExternalImageFormatPropertiesNV',
        'VkImageFormatProperties2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceImageFormatProperties',
    }
    _python_name_ = {
        'maxExtent': 'max_extent',
        'maxMipLevels': 'max_mip_levels',
        'maxArrayLayers': 'max_array_layers',
        'sampleCounts': 'sample_counts',
        'maxResourceSize': 'max_resource_size',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sampleCounts': 'VkSampleCountFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D

VkImageFormatProperties._fields_ = [
    ('maxExtent', VkExtent3D),
    ('maxMipLevels', ctypes.c_uint32),
    ('maxArrayLayers', ctypes.c_uint32),
    ('sampleCounts', ctypes.c_uint32),
    ('maxResourceSize', ctypes.c_uint64),
]

VkImageFormatProperties._type_ = {
    'maxExtent': VkExtent3D,
    'maxMipLevels': ctypes.c_uint32,
    'maxArrayLayers': ctypes.c_uint32,
    'sampleCounts': ctypes.c_uint32,
    'maxResourceSize': ctypes.c_uint64,
}
