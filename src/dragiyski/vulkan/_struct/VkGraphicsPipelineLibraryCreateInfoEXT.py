import ctypes, sys

class VkGraphicsPipelineLibraryCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkGraphicsPipelineLibraryCreateInfoEXT
