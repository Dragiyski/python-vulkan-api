import ctypes

class VkVideoEncodeH265DpbSlotInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoReferenceSlotInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265ReferenceInfo',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pStdReferenceInfo': 'std_reference_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_DPB_SLOT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_DPB_SLOT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH265ReferenceInfo import StdVideoEncodeH265ReferenceInfo

VkVideoEncodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH265ReferenceInfo)),
]

VkVideoEncodeH265DpbSlotInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdReferenceInfo': ctypes.POINTER(StdVideoEncodeH265ReferenceInfo),
}
