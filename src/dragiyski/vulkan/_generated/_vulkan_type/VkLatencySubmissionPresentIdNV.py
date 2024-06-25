import ctypes

class VkLatencySubmissionPresentIdNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
    ]

VkLatencySubmissionPresentIdNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentID': ctypes.c_uint64,
}
