import ctypes

class VkCheckpointData2NV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint64),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

VkCheckpointData2NV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stage': ctypes.c_uint64,
    'pCheckpointMarker': ctypes.c_void_p,
}
