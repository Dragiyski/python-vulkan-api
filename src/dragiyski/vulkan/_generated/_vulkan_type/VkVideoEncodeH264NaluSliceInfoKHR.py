import ctypes

class VkVideoEncodeH264NaluSliceInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264SliceHeader',
    }
    _included_in_ = {
        'VkVideoEncodeH264PictureInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'constantQp': 'constant_qp',
        'pStdSliceHeader': 'std_slice_header',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_NALU_SLICE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_NALU_SLICE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH264SliceHeader import StdVideoEncodeH264SliceHeader

VkVideoEncodeH264NaluSliceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceHeader', ctypes.POINTER(StdVideoEncodeH264SliceHeader)),
]

VkVideoEncodeH264NaluSliceInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'constantQp': ctypes.c_int32,
    'pStdSliceHeader': ctypes.POINTER(StdVideoEncodeH264SliceHeader),
}
