import ctypes, sys

class VkStencilOpState(ctypes.Structure):
    _fields_ = [
        ('failOp', ctypes.c_int),
        ('passOp', ctypes.c_int),
        ('depthFailOp', ctypes.c_int),
        ('compareOp', ctypes.c_int),
        ('compareMask', ctypes.c_uint32),
        ('writeMask', ctypes.c_uint32),
        ('reference', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkStencilOpState
