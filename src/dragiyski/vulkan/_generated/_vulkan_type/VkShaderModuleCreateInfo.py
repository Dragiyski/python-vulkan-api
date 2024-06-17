import ctypes, sys

class VkShaderModuleCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('codeSize', ctypes.c_size_t),
        ('pCode', ctypes.POINTER(ctypes.c_uint32)),
    ]

sys.modules[__name__] = VkShaderModuleCreateInfo
