import ctypes

class VkImageCompressionPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionFlags', ctypes.c_uint32),
        ('imageCompressionFixedRateFlags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkImageFormatProperties2',
        'VkSubresourceLayout2KHR',
        'VkSurfaceFormat2KHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageCompressionFlags': 'image_compression_flags',
        'imageCompressionFixedRateFlags': 'image_compression_fixed_rate_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_compression_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'imageCompressionFlags': 'VkImageCompressionFlagsEXT',
        'imageCompressionFixedRateFlags': 'VkImageCompressionFixedRateFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageCompressionPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageCompressionFlags': ctypes.c_uint32,
    'imageCompressionFixedRateFlags': ctypes.c_uint32,
}
