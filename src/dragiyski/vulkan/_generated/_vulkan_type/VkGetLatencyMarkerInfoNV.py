import ctypes

class CType(ctypes.Structure):
    pass

from .VkLatencyTimingsFrameReportNV import CType as VkLatencyTimingsFrameReportNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]
