import ctypes, sys

class VkClearDepthStencilValue(ctypes.Structure):
    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkClearDepthStencilValue
