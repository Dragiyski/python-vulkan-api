import ctypes

class VkImagePlaneMemoryRequirementsInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('planeAspect', ctypes.c_uint32),
    ]

VkImagePlaneMemoryRequirementsInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'planeAspect': ctypes.c_uint32,
}
