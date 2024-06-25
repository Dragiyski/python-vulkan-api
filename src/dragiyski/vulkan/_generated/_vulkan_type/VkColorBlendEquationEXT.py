import ctypes

class VkColorBlendEquationEXT(ctypes.Structure):
    _fields_ = [
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
    ]

VkColorBlendEquationEXT._type_ = {
    'srcColorBlendFactor': ctypes.c_int,
    'dstColorBlendFactor': ctypes.c_int,
    'colorBlendOp': ctypes.c_int,
    'srcAlphaBlendFactor': ctypes.c_int,
    'dstAlphaBlendFactor': ctypes.c_int,
    'alphaBlendOp': ctypes.c_int,
}
