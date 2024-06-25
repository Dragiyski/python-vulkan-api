import ctypes

class VkPhysicalDeviceShaderCoreBuiltinsFeaturesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreBuiltins', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderCoreBuiltinsFeaturesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderCoreBuiltins': ctypes.c_uint32,
}
