import ctypes, sys

class VkGetLatencyMarkerInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGetLatencyMarkerInfoNV

from . import VkLatencyTimingsFrameReportNV

VkGetLatencyMarkerInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]
