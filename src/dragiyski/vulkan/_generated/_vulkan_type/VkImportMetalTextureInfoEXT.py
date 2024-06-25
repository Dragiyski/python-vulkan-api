import ctypes

class VkImportMetalTextureInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]

VkImportMetalTextureInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'plane': ctypes.c_uint32,
    'mtlTexture': ctypes.c_void_p,
}
