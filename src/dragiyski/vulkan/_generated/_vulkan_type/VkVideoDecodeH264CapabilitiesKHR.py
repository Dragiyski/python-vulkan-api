import ctypes

class VkVideoDecodeH264CapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoCapabilitiesKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkOffset2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxLevelIdc': 'max_level_idc',
        'fieldOffsetGranularity': 'field_offset_granularity',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'maxLevelIdc': 'StdVideoH264LevelIdc',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkOffset2D import VkOffset2D

VkVideoDecodeH264CapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxLevelIdc', ctypes.c_int),
    ('fieldOffsetGranularity', VkOffset2D),
]

VkVideoDecodeH264CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevelIdc': ctypes.c_int,
    'fieldOffsetGranularity': VkOffset2D,
}
