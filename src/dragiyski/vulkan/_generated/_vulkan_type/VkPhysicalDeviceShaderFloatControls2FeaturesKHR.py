import ctypes

class VkPhysicalDeviceShaderFloatControls2FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderFloatControls2', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderFloatControls2FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderFloatControls2': ctypes.c_uint32,
}
