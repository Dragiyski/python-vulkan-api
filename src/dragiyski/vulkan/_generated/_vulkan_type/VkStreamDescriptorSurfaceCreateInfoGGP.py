import ctypes

class VkStreamDescriptorSurfaceCreateInfoGGP(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('streamDescriptor', ctypes.c_uint32),
    ]

VkStreamDescriptorSurfaceCreateInfoGGP._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'streamDescriptor': ctypes.c_uint32,
}
