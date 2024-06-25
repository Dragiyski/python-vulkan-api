import ctypes

class VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderEarlyAndLateFragmentTests', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderEarlyAndLateFragmentTestsFeaturesAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderEarlyAndLateFragmentTests': ctypes.c_uint32,
}
