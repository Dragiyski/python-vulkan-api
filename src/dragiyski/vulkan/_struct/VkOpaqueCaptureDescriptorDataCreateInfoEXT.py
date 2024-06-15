import ctypes, sys

class VkOpaqueCaptureDescriptorDataCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opaqueCaptureDescriptorData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkOpaqueCaptureDescriptorDataCreateInfoEXT
