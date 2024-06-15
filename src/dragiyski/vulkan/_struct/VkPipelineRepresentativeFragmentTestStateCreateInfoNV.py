import ctypes, sys

class VkPipelineRepresentativeFragmentTestStateCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('representativeFragmentTestEnable', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPipelineRepresentativeFragmentTestStateCreateInfoNV
