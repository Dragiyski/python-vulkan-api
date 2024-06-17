import ctypes, sys

class VkImageViewCaptureDescriptorDataInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImageViewCaptureDescriptorDataInfoEXT
