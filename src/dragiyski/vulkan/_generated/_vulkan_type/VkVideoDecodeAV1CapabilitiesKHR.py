import ctypes

class VkVideoDecodeAV1CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevel', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoCapabilitiesKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxLevel': 'max_level',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_av1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'maxLevel': 'StdVideoAV1Level',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoDecodeAV1CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevel': ctypes.c_int,
}
