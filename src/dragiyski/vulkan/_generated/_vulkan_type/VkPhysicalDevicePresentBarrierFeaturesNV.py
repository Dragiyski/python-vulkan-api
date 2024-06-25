import ctypes

class VkPhysicalDevicePresentBarrierFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentBarrier', ctypes.c_uint32),
    ]

VkPhysicalDevicePresentBarrierFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentBarrier': ctypes.c_uint32,
}
