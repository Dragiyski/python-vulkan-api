import ctypes

class VkPhysicalDeviceCopyMemoryIndirectFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('indirectCopy', ctypes.c_uint32),
    ]

VkPhysicalDeviceCopyMemoryIndirectFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'indirectCopy': ctypes.c_uint32,
}
