import ctypes

class VkVideoEncodeH264RateControlLayerInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'useMinQp': ctypes.c_uint32,
            'minQp': VkVideoEncodeH264QpKHR,
            'useMaxQp': ctypes.c_uint32,
            'maxQp': VkVideoEncodeH264QpKHR,
            'useMaxFrameSize': ctypes.c_uint32,
            'maxFrameSize': VkVideoEncodeH264FrameSizeKHR,
        }


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
