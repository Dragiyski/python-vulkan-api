import ctypes

class VkQueryLowLatencySupportNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pQueriedLowLatencyData', ctypes.c_void_p),
    ]

VkQueryLowLatencySupportNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pQueriedLowLatencyData': ctypes.c_void_p,
}
