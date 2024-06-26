import ctypes

class VkVideoDecodeH265PictureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoDecodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoDecodeH265PictureInfo',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pStdPictureInfo': 'std_picture_info',
        'sliceSegmentCount': 'slice_segment_count',
        'pSliceSegmentOffsets': 'slice_segment_offsets',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PICTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PICTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoDecodeH265PictureInfo import StdVideoDecodeH265PictureInfo

VkVideoDecodeH265PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH265PictureInfo)),
    ('sliceSegmentCount', ctypes.c_uint32),
    ('pSliceSegmentOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

VkVideoDecodeH265PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeH265PictureInfo),
    'sliceSegmentCount': ctypes.c_uint32,
    'pSliceSegmentOffsets': ctypes.POINTER(ctypes.c_uint32),
}
