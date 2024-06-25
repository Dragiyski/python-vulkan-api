import ctypes

class VkLatencyTimingsFrameReportNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
        ('inputSampleTimeUs', ctypes.c_uint64),
        ('simStartTimeUs', ctypes.c_uint64),
        ('simEndTimeUs', ctypes.c_uint64),
        ('renderSubmitStartTimeUs', ctypes.c_uint64),
        ('renderSubmitEndTimeUs', ctypes.c_uint64),
        ('presentStartTimeUs', ctypes.c_uint64),
        ('presentEndTimeUs', ctypes.c_uint64),
        ('driverStartTimeUs', ctypes.c_uint64),
        ('driverEndTimeUs', ctypes.c_uint64),
        ('osRenderQueueStartTimeUs', ctypes.c_uint64),
        ('osRenderQueueEndTimeUs', ctypes.c_uint64),
        ('gpuRenderStartTimeUs', ctypes.c_uint64),
        ('gpuRenderEndTimeUs', ctypes.c_uint64),
    ]

VkLatencyTimingsFrameReportNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentID': ctypes.c_uint64,
    'inputSampleTimeUs': ctypes.c_uint64,
    'simStartTimeUs': ctypes.c_uint64,
    'simEndTimeUs': ctypes.c_uint64,
    'renderSubmitStartTimeUs': ctypes.c_uint64,
    'renderSubmitEndTimeUs': ctypes.c_uint64,
    'presentStartTimeUs': ctypes.c_uint64,
    'presentEndTimeUs': ctypes.c_uint64,
    'driverStartTimeUs': ctypes.c_uint64,
    'driverEndTimeUs': ctypes.c_uint64,
    'osRenderQueueStartTimeUs': ctypes.c_uint64,
    'osRenderQueueEndTimeUs': ctypes.c_uint64,
    'gpuRenderStartTimeUs': ctypes.c_uint64,
    'gpuRenderEndTimeUs': ctypes.c_uint64,
}
