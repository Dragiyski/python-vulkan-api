import ctypes

class VkPhysicalDeviceShaderCorePropertiesARM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pixelRate', ctypes.c_uint32),
        ('texelRate', ctypes.c_uint32),
        ('fmaRate', ctypes.c_uint32),
    ]

VkPhysicalDeviceShaderCorePropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pixelRate': ctypes.c_uint32,
    'texelRate': ctypes.c_uint32,
    'fmaRate': ctypes.c_uint32,
}
