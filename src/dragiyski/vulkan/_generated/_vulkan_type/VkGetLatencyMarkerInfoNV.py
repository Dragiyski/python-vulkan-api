import ctypes

class VkGetLatencyMarkerInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'timingCount': ctypes.c_uint32,
            'pTimings': ctypes.POINTER(VkLatencyTimingsFrameReportNV),
        }


from .VkLatencyTimingsFrameReportNV import VkLatencyTimingsFrameReportNV

VkGetLatencyMarkerInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('timingCount', ctypes.c_uint32),
    ('pTimings', ctypes.POINTER(VkLatencyTimingsFrameReportNV)),
]
