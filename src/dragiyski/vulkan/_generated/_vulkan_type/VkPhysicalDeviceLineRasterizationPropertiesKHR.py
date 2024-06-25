import ctypes

class VkPhysicalDeviceLineRasterizationPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lineSubPixelPrecisionBits', ctypes.c_uint32),
    ]

VkPhysicalDeviceLineRasterizationPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'lineSubPixelPrecisionBits': ctypes.c_uint32,
}
