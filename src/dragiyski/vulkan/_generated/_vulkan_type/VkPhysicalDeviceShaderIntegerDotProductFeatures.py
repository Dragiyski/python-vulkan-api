import ctypes

class VkPhysicalDeviceShaderIntegerDotProductFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderIntegerDotProduct', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderIntegerDotProductFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderIntegerDotProduct': ctypes.c_uint32,
}
