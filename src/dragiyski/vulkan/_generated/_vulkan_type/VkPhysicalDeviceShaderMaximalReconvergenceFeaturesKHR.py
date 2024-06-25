import ctypes

class VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderMaximalReconvergence', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderMaximalReconvergenceFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderMaximalReconvergence': ctypes.c_uint32,
}
