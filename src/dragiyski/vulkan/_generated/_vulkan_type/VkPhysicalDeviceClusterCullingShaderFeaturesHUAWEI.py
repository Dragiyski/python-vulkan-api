import ctypes

class VkPhysicalDeviceClusterCullingShaderFeaturesHUAWEI(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'clustercullingShader': ctypes.c_uint32,
            'multiviewClusterCullingShader': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clustercullingShader', ctypes.c_uint32),
        ('multiviewClusterCullingShader', ctypes.c_uint32),
    ]
