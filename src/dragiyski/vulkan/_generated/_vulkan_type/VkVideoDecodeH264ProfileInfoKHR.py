import ctypes

class VkVideoDecodeH264ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
        ('pictureLayout', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkQueryPoolCreateInfo',
        'VkVideoProfileInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stdProfileIdc': 'std_profile_idc',
        'pictureLayout': 'picture_layout',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stdProfileIdc': 'StdVideoH264ProfileIdc',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PROFILE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PROFILE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoDecodeH264ProfileInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdProfileIdc': ctypes.c_int,
    'pictureLayout': ctypes.c_uint32,
}
