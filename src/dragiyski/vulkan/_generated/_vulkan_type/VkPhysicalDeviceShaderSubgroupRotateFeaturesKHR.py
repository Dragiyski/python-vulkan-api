import ctypes

class VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupRotate', ctypes.c_uint32),
        ('shaderSubgroupRotateClustered', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderSubgroupRotate': ctypes.c_uint32,
    'shaderSubgroupRotateClustered': ctypes.c_uint32,
}
