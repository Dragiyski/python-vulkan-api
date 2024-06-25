import ctypes

class VkPhysicalDeviceDepthClipControlFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthClipControl', ctypes.c_uint32),
    ]

VkPhysicalDeviceDepthClipControlFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthClipControl': ctypes.c_uint32,
}
