import ctypes, sys

class VkPipelineColorWriteCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pColorWriteEnables', ctypes.POINTER(ctypes.c_uint32)),
    ]

sys.modules[__name__] = VkPipelineColorWriteCreateInfoEXT
