import ctypes

class VkPhysicalDeviceImageRobustnessFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustImageAccess', ctypes.c_uint32),
    ]

VkPhysicalDeviceImageRobustnessFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'robustImageAccess': ctypes.c_uint32,
}
