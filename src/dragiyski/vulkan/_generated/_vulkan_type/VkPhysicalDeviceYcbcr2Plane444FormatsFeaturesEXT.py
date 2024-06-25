import ctypes

class VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ycbcr2plane444Formats', ctypes.c_uint32),
    ]

VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'ycbcr2plane444Formats': ctypes.c_uint32,
}
