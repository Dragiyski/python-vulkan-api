import ctypes, sys

class VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clusterShadingRate', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceClusterCullingShaderVrsFeaturesHUAWEI
