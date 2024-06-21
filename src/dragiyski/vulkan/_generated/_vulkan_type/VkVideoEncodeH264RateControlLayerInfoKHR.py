import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH264FrameSizeKHR import CType as VkVideoEncodeH264FrameSizeKHR
from .VkVideoEncodeH264QpKHR import CType as VkVideoEncodeH264QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH264QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH264QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH264FrameSizeKHR),
]
