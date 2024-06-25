import ctypes

class VkPhysicalDeviceShaderSMBuiltinsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSMBuiltins', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderSMBuiltinsFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderSMBuiltins': ctypes.c_uint32,
}
