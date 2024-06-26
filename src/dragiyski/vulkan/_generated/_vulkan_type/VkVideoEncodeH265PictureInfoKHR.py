import ctypes

class VkVideoEncodeH265PictureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoEncodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265PictureInfo',
        'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'naluSliceSegmentEntryCount': 'nalu_slice_segment_entry_count',
        'pNaluSliceSegmentEntries': 'nalu_slice_segment_entries',
        'pStdPictureInfo': 'std_picture_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PICTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PICTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH265PictureInfo import StdVideoEncodeH265PictureInfo
from .VkVideoEncodeH265NaluSliceSegmentInfoKHR import VkVideoEncodeH265NaluSliceSegmentInfoKHR

VkVideoEncodeH265PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceSegmentEntryCount', ctypes.c_uint32),
    ('pNaluSliceSegmentEntries', ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH265PictureInfo)),
]

VkVideoEncodeH265PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'naluSliceSegmentEntryCount': ctypes.c_uint32,
    'pNaluSliceSegmentEntries': ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR),
    'pStdPictureInfo': ctypes.POINTER(StdVideoEncodeH265PictureInfo),
}
