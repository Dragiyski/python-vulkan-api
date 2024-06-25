import ctypes

class VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupExtendedTypes', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderSubgroupExtendedTypesFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderSubgroupExtendedTypes': ctypes.c_uint32,
}
