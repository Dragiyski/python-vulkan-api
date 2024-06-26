import ctypes

class VkVideoFormatPropertiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkComponentMapping',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'format': 'format',
        'componentMapping': 'component_mapping',
        'imageCreateFlags': 'image_create_flags',
        'imageType': 'image_type',
        'imageTiling': 'image_tiling',
        'imageUsageFlags': 'image_usage_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'format': 'VkFormat',
        'imageCreateFlags': 'VkImageCreateFlags',
        'imageType': 'VkImageType',
        'imageTiling': 'VkImageTiling',
        'imageUsageFlags': 'VkImageUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_FORMAT_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_FORMAT_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkComponentMapping import VkComponentMapping

VkVideoFormatPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('componentMapping', VkComponentMapping),
    ('imageCreateFlags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('imageTiling', ctypes.c_int),
    ('imageUsageFlags', ctypes.c_uint32),
]

VkVideoFormatPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'format': ctypes.c_int,
    'componentMapping': VkComponentMapping,
    'imageCreateFlags': ctypes.c_uint32,
    'imageType': ctypes.c_int,
    'imageTiling': ctypes.c_int,
    'imageUsageFlags': ctypes.c_uint32,
}
