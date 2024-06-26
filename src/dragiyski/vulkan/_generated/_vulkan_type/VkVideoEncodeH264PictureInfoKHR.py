import ctypes

class VkVideoEncodeH264PictureInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoEncodeInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264PictureInfo',
        'VkVideoEncodeH264NaluSliceInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'naluSliceEntryCount': 'nalu_slice_entry_count',
        'pNaluSliceEntries': 'nalu_slice_entries',
        'pStdPictureInfo': 'std_picture_info',
        'generatePrefixNalu': 'generate_prefix_nalu',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PICTURE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PICTURE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH264PictureInfo import StdVideoEncodeH264PictureInfo
from .VkVideoEncodeH264NaluSliceInfoKHR import VkVideoEncodeH264NaluSliceInfoKHR

VkVideoEncodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceEntryCount', ctypes.c_uint32),
    ('pNaluSliceEntries', ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH264PictureInfo)),
    ('generatePrefixNalu', ctypes.c_uint32),
]

VkVideoEncodeH264PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'naluSliceEntryCount': ctypes.c_uint32,
    'pNaluSliceEntries': ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR),
    'pStdPictureInfo': ctypes.POINTER(StdVideoEncodeH264PictureInfo),
    'generatePrefixNalu': ctypes.c_uint32,
}
