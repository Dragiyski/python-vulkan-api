import ctypes

class VkPhysicalDeviceShaderRelaxedExtendedInstructionFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderRelaxedExtendedInstruction', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderRelaxedExtendedInstructionFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderRelaxedExtendedInstruction': ctypes.c_uint32,
}
