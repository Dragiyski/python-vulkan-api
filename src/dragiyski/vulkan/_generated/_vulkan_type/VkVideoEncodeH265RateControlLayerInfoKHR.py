import ctypes

class VkVideoEncodeH265RateControlLayerInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoEncodeRateControlLayerInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoEncodeH265FrameSizeKHR',
        'VkVideoEncodeH265QpKHR',
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
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_LAYER_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_LAYER_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoEncodeH265FrameSizeKHR import VkVideoEncodeH265FrameSizeKHR
from .VkVideoEncodeH265QpKHR import VkVideoEncodeH265QpKHR

VkVideoEncodeH265RateControlLayerInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH265QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH265QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH265FrameSizeKHR),
]

VkVideoEncodeH265RateControlLayerInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useMinQp': ctypes.c_uint32,
    'minQp': VkVideoEncodeH265QpKHR,
    'useMaxQp': ctypes.c_uint32,
    'maxQp': VkVideoEncodeH265QpKHR,
    'useMaxFrameSize': ctypes.c_uint32,
    'maxFrameSize': VkVideoEncodeH265FrameSizeKHR,
}
