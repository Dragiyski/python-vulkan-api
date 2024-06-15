import ctypes, sys

class VkVideoFormatPropertiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoFormatPropertiesKHR

from . import VkComponentMapping

VkVideoFormatPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('componentMapping', VkComponentMapping),
    ('imageCreateFlags', ctypes.c_uint32),
    ('imageType', ctypes.c_int),
    ('imageTiling', ctypes.c_int),
    ('imageUsageFlags', ctypes.c_uint32),
]
