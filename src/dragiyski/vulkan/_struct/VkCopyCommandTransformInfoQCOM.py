import ctypes, sys

class VkCopyCommandTransformInfoQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('transform', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkCopyCommandTransformInfoQCOM
