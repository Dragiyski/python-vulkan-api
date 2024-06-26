import ctypes

class VkVideoEncodeH265RateControlInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('gopFrameCount', ctypes.c_uint32),
        ('idrPeriod', ctypes.c_uint32),
        ('consecutiveBFrameCount', ctypes.c_uint32),
        ('subLayerCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoBeginCodingInfoKHR',
        'VkVideoCodingControlInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'gopFrameCount': 'gop_frame_count',
        'idrPeriod': 'idr_period',
        'consecutiveBFrameCount': 'consecutive_bframe_count',
        'subLayerCount': 'sub_layer_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEncodeH265RateControlFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH265RateControlInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'gopFrameCount': ctypes.c_uint32,
    'idrPeriod': ctypes.c_uint32,
    'consecutiveBFrameCount': ctypes.c_uint32,
    'subLayerCount': ctypes.c_uint32,
}
