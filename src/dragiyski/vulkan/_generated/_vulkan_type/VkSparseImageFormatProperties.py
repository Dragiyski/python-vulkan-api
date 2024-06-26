import ctypes

class VkSparseImageFormatProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
    }
    _included_in_ = {
        'VkSparseImageFormatProperties2',
        'VkSparseImageMemoryRequirements',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSparseImageFormatProperties',
    }
    _python_name_ = {
        'aspectMask': 'aspect_mask',
        'imageGranularity': 'image_granularity',
        'flags': 'flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'aspectMask': 'VkImageAspectFlags',
        'flags': 'VkSparseImageFormatFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D

VkSparseImageFormatProperties._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]

VkSparseImageFormatProperties._type_ = {
    'aspectMask': ctypes.c_uint32,
    'imageGranularity': VkExtent3D,
    'flags': ctypes.c_uint32,
}
