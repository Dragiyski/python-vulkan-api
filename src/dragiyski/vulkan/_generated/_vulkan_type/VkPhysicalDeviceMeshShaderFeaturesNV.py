import ctypes

class VkPhysicalDeviceMeshShaderFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('taskShader', ctypes.c_uint32),
        ('meshShader', ctypes.c_uint32),
    ]

VkPhysicalDeviceMeshShaderFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'taskShader': ctypes.c_uint32,
    'meshShader': ctypes.c_uint32,
}
