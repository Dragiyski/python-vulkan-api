import ctypes

class VkPhysicalDevicePortabilitySubsetPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minVertexInputBindingStrideAlignment', ctypes.c_uint32),
    ]

VkPhysicalDevicePortabilitySubsetPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minVertexInputBindingStrideAlignment': ctypes.c_uint32,
}
