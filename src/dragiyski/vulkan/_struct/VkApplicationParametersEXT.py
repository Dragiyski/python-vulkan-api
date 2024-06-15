import ctypes, sys

class VkApplicationParametersEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('key', ctypes.c_uint32),
        ('value', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkApplicationParametersEXT