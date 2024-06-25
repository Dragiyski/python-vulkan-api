import ctypes

class VkPhysicalDeviceShaderObjectFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderObject', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderObjectFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shaderObject': ctypes.c_uint32,
}
