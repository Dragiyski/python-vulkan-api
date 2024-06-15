import ctypes, sys

class VkCopyMicromapToMemoryInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyMicromapToMemoryInfoEXT

from . import VkDeviceOrHostAddressKHR

VkCopyMicromapToMemoryInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]
