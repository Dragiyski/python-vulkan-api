import ctypes

class VkPhysicalDeviceSamplerFilterMinmaxProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterMinmaxSingleComponentFormats', ctypes.c_uint32),
        ('filterMinmaxImageComponentMapping', ctypes.c_uint32),
    ]

VkPhysicalDeviceSamplerFilterMinmaxProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'filterMinmaxSingleComponentFormats': ctypes.c_uint32,
    'filterMinmaxImageComponentMapping': ctypes.c_uint32,
}
