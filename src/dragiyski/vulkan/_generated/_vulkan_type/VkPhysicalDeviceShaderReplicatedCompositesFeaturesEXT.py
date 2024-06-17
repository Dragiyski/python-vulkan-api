import ctypes, sys

class VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderReplicatedComposites', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderReplicatedCompositesFeaturesEXT
