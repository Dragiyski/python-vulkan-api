import ctypes

class VkPhysicalDeviceInvocationMaskFeaturesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('invocationMask', ctypes.c_uint32),
    ]

VkPhysicalDeviceInvocationMaskFeaturesHUAWEI._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'invocationMask': ctypes.c_uint32,
}
