import ctypes

class VkVideoProfileListInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkBufferCreateInfo',
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
        'VkPhysicalDeviceVideoFormatInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoProfileInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'profileCount': 'profile_count',
        'pProfiles': 'profiles',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_LIST_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PROFILE_LIST_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkVideoProfileListInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]

VkVideoProfileListInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'profileCount': ctypes.c_uint32,
    'pProfiles': ctypes.POINTER(VkVideoProfileInfoKHR),
}
