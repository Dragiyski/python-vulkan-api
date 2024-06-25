import ctypes

class VkPhysicalDeviceImageAlignmentControlPropertiesMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedImageAlignmentMask', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageAlignmentControlPropertiesMESA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportedImageAlignmentMask': ctypes.c_uint32,
}
