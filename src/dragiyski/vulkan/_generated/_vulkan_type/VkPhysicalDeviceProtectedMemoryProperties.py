import ctypes

class VkPhysicalDeviceProtectedMemoryProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('protectedNoFault', ctypes.c_uint32),
    ]

VkPhysicalDeviceProtectedMemoryProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'protectedNoFault': ctypes.c_uint32,
}
