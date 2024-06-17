import ctypes, sys

class VkTextureLODGatherFormatPropertiesAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportsTextureGatherLODBiasAMD', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkTextureLODGatherFormatPropertiesAMD
