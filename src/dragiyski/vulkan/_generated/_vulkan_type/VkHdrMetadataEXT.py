import ctypes

class VkHdrMetadataEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkXYColorEXT',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkSetHdrMetadataEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'displayPrimaryRed': 'display_primary_red',
        'displayPrimaryGreen': 'display_primary_green',
        'displayPrimaryBlue': 'display_primary_blue',
        'whitePoint': 'white_point',
        'maxLuminance': 'max_luminance',
        'minLuminance': 'min_luminance',
        'maxContentLightLevel': 'max_content_light_level',
        'maxFrameAverageLightLevel': 'max_frame_average_light_level',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_hdr_metadata',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_HDR_METADATA_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_HDR_METADATA_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkXYColorEXT import VkXYColorEXT

VkHdrMetadataEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPrimaryRed', VkXYColorEXT),
    ('displayPrimaryGreen', VkXYColorEXT),
    ('displayPrimaryBlue', VkXYColorEXT),
    ('whitePoint', VkXYColorEXT),
    ('maxLuminance', ctypes.c_float),
    ('minLuminance', ctypes.c_float),
    ('maxContentLightLevel', ctypes.c_float),
    ('maxFrameAverageLightLevel', ctypes.c_float),
]

VkHdrMetadataEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayPrimaryRed': VkXYColorEXT,
    'displayPrimaryGreen': VkXYColorEXT,
    'displayPrimaryBlue': VkXYColorEXT,
    'whitePoint': VkXYColorEXT,
    'maxLuminance': ctypes.c_float,
    'minLuminance': ctypes.c_float,
    'maxContentLightLevel': ctypes.c_float,
    'maxFrameAverageLightLevel': ctypes.c_float,
}
