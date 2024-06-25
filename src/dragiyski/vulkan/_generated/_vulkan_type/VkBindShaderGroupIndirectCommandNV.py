import ctypes

class VkBindShaderGroupIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]

VkBindShaderGroupIndirectCommandNV._type_ = {
    'groupIndex': ctypes.c_uint32,
}
