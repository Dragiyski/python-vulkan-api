import ctypes

class VkPhysicalDeviceShaderDrawParametersFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderDrawParameters', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderDrawParametersFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderDrawParameters': ctypes.c_uint32,
}
