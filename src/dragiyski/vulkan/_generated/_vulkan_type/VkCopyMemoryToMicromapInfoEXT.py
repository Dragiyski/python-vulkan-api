import ctypes, sys

class VkCopyMemoryToMicromapInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyMemoryToMicromapInfoEXT

from . import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToMicromapInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]
