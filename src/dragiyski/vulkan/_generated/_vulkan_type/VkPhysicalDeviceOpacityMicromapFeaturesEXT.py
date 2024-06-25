import ctypes

class VkPhysicalDeviceOpacityMicromapFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('micromap', ctypes.c_uint32),
        ('micromapCaptureReplay', ctypes.c_uint32),
        ('micromapHostCommands', ctypes.c_uint32),
    ]

VkPhysicalDeviceOpacityMicromapFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'micromap': ctypes.c_uint32,
    'micromapCaptureReplay': ctypes.c_uint32,
    'micromapHostCommands': ctypes.c_uint32,
}
