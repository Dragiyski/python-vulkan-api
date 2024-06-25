import ctypes

class VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderDemoteToHelperInvocation', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderDemoteToHelperInvocationFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderDemoteToHelperInvocation': ctypes.c_uint32,
}
