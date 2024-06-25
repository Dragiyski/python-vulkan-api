import ctypes

class VkPhysicalDeviceExclusiveScissorFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exclusiveScissor', ctypes.c_uint32),
    ]

VkPhysicalDeviceExclusiveScissorFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exclusiveScissor': ctypes.c_uint32,
}
