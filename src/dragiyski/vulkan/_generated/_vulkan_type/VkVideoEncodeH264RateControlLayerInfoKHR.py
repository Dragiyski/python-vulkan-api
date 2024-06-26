import ctypes

class VkVideoEncodeH264RateControlLayerInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoEncodeRateControlLayerInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoEncodeH264FrameSizeKHR',
        'VkVideoEncodeH264QpKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'useMinQp': 'use_min_qp',
        'minQp': 'min_qp',
        'useMaxQp': 'use_max_qp',
        'maxQp': 'max_qp',
        'useMaxFrameSize': 'use_max_frame_size',
        'maxFrameSize': 'max_frame_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_LAYER_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_LAYER_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoEncodeH264FrameSizeKHR import VkVideoEncodeH264FrameSizeKHR
from .VkVideoEncodeH264QpKHR import VkVideoEncodeH264QpKHR

VkVideoEncodeH264RateControlLayerInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH264QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH264QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH264FrameSizeKHR),
]

VkVideoEncodeH264RateControlLayerInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useMinQp': ctypes.c_uint32,
    'minQp': VkVideoEncodeH264QpKHR,
    'useMaxQp': ctypes.c_uint32,
    'maxQp': VkVideoEncodeH264QpKHR,
    'useMaxFrameSize': ctypes.c_uint32,
    'maxFrameSize': VkVideoEncodeH264FrameSizeKHR,
}
