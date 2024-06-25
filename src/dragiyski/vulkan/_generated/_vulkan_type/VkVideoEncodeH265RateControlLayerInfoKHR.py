import ctypes

class VkVideoEncodeH265RateControlLayerInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'useMinQp': ctypes.c_uint32,
            'minQp': VkVideoEncodeH265QpKHR,
            'useMaxQp': ctypes.c_uint32,
            'maxQp': VkVideoEncodeH265QpKHR,
            'useMaxFrameSize': ctypes.c_uint32,
            'maxFrameSize': VkVideoEncodeH265FrameSizeKHR,
        }


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
