import ctypes

class VkPhysicalDeviceImageDrmFormatModifierInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifier', ctypes.c_uint64),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceImageFormatInfo2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'drmFormatModifier': 'drm_format_modifier',
        'sharingMode': 'sharing_mode',
        'queueFamilyIndexCount': 'queue_family_index_count',
        'pQueueFamilyIndices': 'queue_family_indices',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_drm_format_modifier',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'sharingMode': 'VkSharingMode',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceImageDrmFormatModifierInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifier': ctypes.c_uint64,
    'sharingMode': ctypes.c_int,
    'queueFamilyIndexCount': ctypes.c_uint32,
    'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
}
