import ctypes

class VkTextureLODGatherFormatPropertiesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportsTextureGatherLODBiasAMD', ctypes.c_uint32),
    ]

VkTextureLODGatherFormatPropertiesAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportsTextureGatherLODBiasAMD': ctypes.c_uint32,
}
