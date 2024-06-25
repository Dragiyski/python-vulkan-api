import ctypes

class VkImageAlignmentControlCreateInfoMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maximumRequestedAlignment', ctypes.c_uint32),
    ]

VkImageAlignmentControlCreateInfoMESA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maximumRequestedAlignment': ctypes.c_uint32,
}
