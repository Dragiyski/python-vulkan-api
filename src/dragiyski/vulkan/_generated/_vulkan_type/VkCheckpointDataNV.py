import ctypes

class VkCheckpointDataNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint32),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

VkCheckpointDataNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stage': ctypes.c_uint32,
    'pCheckpointMarker': ctypes.c_void_p,
}
