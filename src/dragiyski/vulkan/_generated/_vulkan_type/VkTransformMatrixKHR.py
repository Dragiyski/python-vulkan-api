import ctypes, sys

class VkTransformMatrixKHR(ctypes.Structure):
    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]

sys.modules[__name__] = VkTransformMatrixKHR
