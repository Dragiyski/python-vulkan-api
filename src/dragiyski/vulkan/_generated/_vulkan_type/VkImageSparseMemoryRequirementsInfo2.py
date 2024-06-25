import ctypes

class VkImageSparseMemoryRequirementsInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
    ]

VkImageSparseMemoryRequirementsInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'image': ctypes.c_void_p,
}
