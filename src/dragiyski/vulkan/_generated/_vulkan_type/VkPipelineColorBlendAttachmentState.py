import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('blendEnable', ctypes.c_uint32),
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
        ('colorWriteMask', ctypes.c_uint32),
    ]
