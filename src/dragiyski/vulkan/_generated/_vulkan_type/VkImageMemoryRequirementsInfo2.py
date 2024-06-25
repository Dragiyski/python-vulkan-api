import ctypes

class VkImageMemoryRequirementsInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
    ]

VkImageMemoryRequirementsInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image': ctypes.c_void_p,
}
