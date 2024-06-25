import ctypes

class VkPhysicalDeviceDepthClipEnableFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthClipEnable', ctypes.c_uint32),
    ]

VkPhysicalDeviceDepthClipEnableFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthClipEnable': ctypes.c_uint32,
}
