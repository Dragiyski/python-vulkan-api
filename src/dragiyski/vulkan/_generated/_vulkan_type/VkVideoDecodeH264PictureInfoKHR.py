import ctypes

class VkVideoDecodeH264PictureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoDecodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH264PictureInfo',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pStdPictureInfo': 'std_picture_info',
        'sliceCount': 'slice_count',
        'pSliceOffsets': 'slice_offsets',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PICTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PICTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeH264PictureInfo import StdVideoDecodeH264PictureInfo

VkVideoDecodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH264PictureInfo)),
    ('sliceCount', ctypes.c_uint32),
    ('pSliceOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

VkVideoDecodeH264PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeH264PictureInfo),
    'sliceCount': ctypes.c_uint32,
    'pSliceOffsets': ctypes.POINTER(ctypes.c_uint32),
}
