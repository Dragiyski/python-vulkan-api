import ctypes

class VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkVideoProfileInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pVideoProfile': 'video_profile',
        'qualityLevel': 'quality_level',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_ENCODE_QUALITY_LEVEL_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pVideoProfile', ctypes.POINTER(VkVideoProfileInfoKHR)),
    ('qualityLevel', ctypes.c_uint32),
]

VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pVideoProfile': ctypes.POINTER(VkVideoProfileInfoKHR),
    'qualityLevel': ctypes.c_uint32,
}
