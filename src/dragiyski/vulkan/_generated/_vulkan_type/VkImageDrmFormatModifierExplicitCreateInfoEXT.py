import ctypes

class VkImageDrmFormatModifierExplicitCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkImageCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkSubresourceLayout',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'drmFormatModifier': 'drm_format_modifier',
        'drmFormatModifierPlaneCount': 'drm_format_modifier_plane_count',
        'pPlaneLayouts': 'plane_layouts',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_drm_format_modifier',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSubresourceLayout import VkSubresourceLayout

VkImageDrmFormatModifierExplicitCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifier', ctypes.c_uint64),
    ('drmFormatModifierPlaneCount', ctypes.c_uint32),
    ('pPlaneLayouts', ctypes.POINTER(VkSubresourceLayout)),
]

VkImageDrmFormatModifierExplicitCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifier': ctypes.c_uint64,
    'drmFormatModifierPlaneCount': ctypes.c_uint32,
    'pPlaneLayouts': ctypes.POINTER(VkSubresourceLayout),
}
