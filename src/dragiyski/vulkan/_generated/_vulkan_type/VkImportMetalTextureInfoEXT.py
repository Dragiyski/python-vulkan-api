import ctypes, sys

class VkImportMetalTextureInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImportMetalTextureInfoEXT
