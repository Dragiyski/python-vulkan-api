import ctypes

class VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clustercullingShader', ctypes.c_uint32),
        ('multiviewClusterCullingShader', ctypes.c_uint32),
    ]

VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'clustercullingShader': ctypes.c_uint32,
    'multiviewClusterCullingShader': ctypes.c_uint32,
}
