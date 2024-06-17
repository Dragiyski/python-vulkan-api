import ctypes, sys

class VkOpticalFlowSessionCreatePrivateDataInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('id', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pPrivateData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkOpticalFlowSessionCreatePrivateDataInfoNV
