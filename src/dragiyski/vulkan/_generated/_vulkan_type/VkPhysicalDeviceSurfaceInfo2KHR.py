import ctypes

class VkPhysicalDeviceSurfaceInfo2KHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

VkPhysicalDeviceSurfaceInfo2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surface': ctypes.c_void_p,
}
