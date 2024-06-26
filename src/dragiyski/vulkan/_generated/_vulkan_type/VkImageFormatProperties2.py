import ctypes

class VkImageFormatProperties2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAndroidHardwareBufferUsageANDROID',
        'VkExternalImageFormatProperties',
        'VkFilterCubicImageViewImageFormatPropertiesEXT',
        'VkHostImageCopyDevicePerformanceQueryEXT',
        'VkImageCompressionPropertiesEXT',
        'VkSamplerYcbcrConversionImageFormatProperties',
        'VkTextureLODGatherFormatPropertiesAMD',
    }
    _includes_ = {
        'VkImageFormatProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceImageFormatProperties2',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageFormatProperties': 'image_format_properties',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageFormatProperties import VkImageFormatProperties

VkImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]

VkImageFormatProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageFormatProperties': VkImageFormatProperties,
}
