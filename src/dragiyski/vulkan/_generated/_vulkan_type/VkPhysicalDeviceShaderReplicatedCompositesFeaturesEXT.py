import ctypes

class VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderReplicatedComposites', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderReplicatedComposites': ctypes.c_uint32,
}
