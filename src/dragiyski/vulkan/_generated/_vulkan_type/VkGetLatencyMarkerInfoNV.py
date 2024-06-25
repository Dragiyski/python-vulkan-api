import ctypes

class VkGetLatencyMarkerInfoNV(ctypes.Structure):
    pass

from .VkLatencyTimingsFrameReportNV import VkLatencyTimingsFrameReportNV

VkGetLatencyMarkerInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]

VkGetLatencyMarkerInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'timingCount': ctypes.c_uint32,
    'pTimings': ctypes.POINTER(VkLatencyTimingsFrameReportNV),
}
