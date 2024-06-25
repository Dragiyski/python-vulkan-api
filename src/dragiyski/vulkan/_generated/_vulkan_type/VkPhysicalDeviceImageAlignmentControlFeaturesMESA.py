import ctypes

class VkPhysicalDeviceImageAlignmentControlFeaturesMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageAlignmentControl', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageAlignmentControlFeaturesMESA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageAlignmentControl': ctypes.c_uint32,
}
