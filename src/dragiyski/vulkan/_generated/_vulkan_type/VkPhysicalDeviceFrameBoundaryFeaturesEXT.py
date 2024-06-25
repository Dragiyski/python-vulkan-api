import ctypes

class VkPhysicalDeviceFrameBoundaryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameBoundary', ctypes.c_uint32),
    ]

VkPhysicalDeviceFrameBoundaryFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'frameBoundary': ctypes.c_uint32,
}
