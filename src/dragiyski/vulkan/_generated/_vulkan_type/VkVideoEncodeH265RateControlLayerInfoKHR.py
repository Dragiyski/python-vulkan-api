import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265FrameSizeKHR import CType as VkVideoEncodeH265FrameSizeKHR
from .VkVideoEncodeH265QpKHR import CType as VkVideoEncodeH265QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH265QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH265QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH265FrameSizeKHR),
]
