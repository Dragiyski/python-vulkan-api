import ctypes

class VkPhysicalDeviceImageViewMinLodFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minLod', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageViewMinLodFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minLod': ctypes.c_uint32,
}
