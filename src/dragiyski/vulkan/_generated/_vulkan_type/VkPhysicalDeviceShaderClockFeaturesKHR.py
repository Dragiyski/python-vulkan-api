import ctypes

class VkPhysicalDeviceShaderClockFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupClock', ctypes.c_uint32),
        ('shaderDeviceClock', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderClockFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderSubgroupClock': ctypes.c_uint32,
    'shaderDeviceClock': ctypes.c_uint32,
}
