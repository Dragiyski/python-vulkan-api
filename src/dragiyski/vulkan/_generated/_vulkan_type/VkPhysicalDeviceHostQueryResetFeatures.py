import ctypes

class VkPhysicalDeviceHostQueryResetFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hostQueryReset', ctypes.c_uint32),
    ]

VkPhysicalDeviceHostQueryResetFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hostQueryReset': ctypes.c_uint32,
}
