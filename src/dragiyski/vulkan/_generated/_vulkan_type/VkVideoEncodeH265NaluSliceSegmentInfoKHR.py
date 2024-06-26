import ctypes

class VkVideoEncodeH265NaluSliceSegmentInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265SliceSegmentHeader',
    }
    _included_in_ = {
        'VkVideoEncodeH265PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'constantQp': 'constant_qp',
        'pStdSliceSegmentHeader': 'std_slice_segment_header',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_NALU_SLICE_SEGMENT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_NALU_SLICE_SEGMENT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH265SliceSegmentHeader import StdVideoEncodeH265SliceSegmentHeader

VkVideoEncodeH265NaluSliceSegmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]

VkVideoEncodeH265NaluSliceSegmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'constantQp': ctypes.c_int32,
    'pStdSliceSegmentHeader': ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader),
}
