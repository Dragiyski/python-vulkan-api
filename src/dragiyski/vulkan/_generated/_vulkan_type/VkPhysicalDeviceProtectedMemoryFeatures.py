import ctypes

class VkPhysicalDeviceProtectedMemoryFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('protectedMemory', ctypes.c_uint32),
    ]

VkPhysicalDeviceProtectedMemoryFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'protectedMemory': ctypes.c_uint32,
}
