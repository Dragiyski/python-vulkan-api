import ctypes

class VkPhysicalDeviceExtendedDynamicStateFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedDynamicState', ctypes.c_uint32),
    ]

VkPhysicalDeviceExtendedDynamicStateFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'extendedDynamicState': ctypes.c_uint32,
}
