import ctypes

class VkPhysicalDeviceFragmentShaderBarycentricPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('triStripVertexOrderIndependentOfProvokingVertex', ctypes.c_uint32),
    ]

VkPhysicalDeviceFragmentShaderBarycentricPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'triStripVertexOrderIndependentOfProvokingVertex': ctypes.c_uint32,
}
