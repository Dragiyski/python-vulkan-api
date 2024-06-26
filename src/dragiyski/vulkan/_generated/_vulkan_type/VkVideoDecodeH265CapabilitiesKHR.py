import ctypes

class VkVideoDecodeH265CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevelIdc', ctypes.c_int),
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
        'maxLevelIdc': 'max_level_idc',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'maxLevelIdc': 'StdVideoH265LevelIdc',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoDecodeH265CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevelIdc': ctypes.c_int,
}
