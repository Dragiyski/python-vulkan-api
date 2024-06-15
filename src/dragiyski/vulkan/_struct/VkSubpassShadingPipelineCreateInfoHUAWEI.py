import ctypes, sys

class VkSubpassShadingPipelineCreateInfoHUAWEI(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPass', ctypes.c_void_p),
        ('subpass', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSubpassShadingPipelineCreateInfoHUAWEI
