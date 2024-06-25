import ctypes

class VkPhysicalDeviceDepthClampZeroOneFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthClampZeroOne', ctypes.c_uint32),
    ]

VkPhysicalDeviceDepthClampZeroOneFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthClampZeroOne': ctypes.c_uint32,
}
