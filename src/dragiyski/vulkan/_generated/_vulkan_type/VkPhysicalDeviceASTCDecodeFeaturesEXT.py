import ctypes

class VkPhysicalDeviceASTCDecodeFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decodeModeSharedExponent', ctypes.c_uint32),
    ]

VkPhysicalDeviceASTCDecodeFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'decodeModeSharedExponent': ctypes.c_uint32,
}
