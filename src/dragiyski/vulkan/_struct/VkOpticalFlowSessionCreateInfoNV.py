import ctypes, sys

class VkOpticalFlowSessionCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('imageFormat', ctypes.c_int),
        ('flowVectorFormat', ctypes.c_int),
        ('costFormat', ctypes.c_int),
        ('outputGridSize', ctypes.c_uint32),
        ('hintGridSize', ctypes.c_uint32),
        ('performanceLevel', ctypes.c_int),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkOpticalFlowSessionCreateInfoNV