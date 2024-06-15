import ctypes, sys

class VkSamplerCaptureDescriptorDataInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sampler', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkSamplerCaptureDescriptorDataInfoEXT
