import ctypes, sys

class VkCopyMemoryToAccelerationStructureInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyMemoryToAccelerationStructureInfoKHR

from . import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]
