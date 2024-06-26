import ctypes

class VkImageFormatConstraintsInfoFUCHSIA(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkImageCreateInfo',
        'VkSysmemColorSpaceFUCHSIA',
    }
    _included_in_ = {
        'VkImageConstraintsInfoFUCHSIA',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageCreateInfo': 'image_create_info',
        'requiredFormatFeatures': 'required_format_features',
        'flags': 'flags',
        'sysmemPixelFormat': 'sysmem_pixel_format',
        'colorSpaceCount': 'color_space_count',
        'pColorSpaces': 'color_spaces',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_FUCHSIA_buffer_collection',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'requiredFormatFeatures': 'VkFormatFeatureFlags',
        'flags': 'VkImageFormatConstraintsFlagsFUCHSIA',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_CONSTRAINTS_INFO_FUCHSIA'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_IMAGE_FORMAT_CONSTRAINTS_INFO_FUCHSIA
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkImageCreateInfo import VkImageCreateInfo
from .VkSysmemColorSpaceFUCHSIA import VkSysmemColorSpaceFUCHSIA

VkImageFormatConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageCreateInfo', VkImageCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('colorSpaceCount', ctypes.c_uint32),
    ('pColorSpaces', ctypes.POINTER(VkSysmemColorSpaceFUCHSIA)),
]

VkImageFormatConstraintsInfoFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageCreateInfo': VkImageCreateInfo,
    'requiredFormatFeatures': ctypes.c_uint32,
    'flags': ctypes.c_uint32,
    'sysmemPixelFormat': ctypes.c_uint64,
    'colorSpaceCount': ctypes.c_uint32,
    'pColorSpaces': ctypes.POINTER(VkSysmemColorSpaceFUCHSIA),
}
