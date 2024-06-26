import ctypes

class VkDrmFormatModifierPropertiesList2EXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkFormatProperties2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkDrmFormatModifierProperties2EXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'drmFormatModifierCount': 'drm_format_modifier_count',
        'pDrmFormatModifierProperties': 'drm_format_modifier_properties',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_image_drm_format_modifier',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_2_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_2_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDrmFormatModifierProperties2EXT import VkDrmFormatModifierProperties2EXT

VkDrmFormatModifierPropertiesList2EXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]

VkDrmFormatModifierPropertiesList2EXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifierCount': ctypes.c_uint32,
    'pDrmFormatModifierProperties': ctypes.POINTER(VkDrmFormatModifierProperties2EXT),
}
