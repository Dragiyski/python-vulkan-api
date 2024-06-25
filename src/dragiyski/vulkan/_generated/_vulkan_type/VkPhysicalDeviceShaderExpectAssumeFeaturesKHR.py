import ctypes

class VkPhysicalDeviceShaderExpectAssumeFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderExpectAssume', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderExpectAssumeFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderExpectAssume': ctypes.c_uint32,
}
