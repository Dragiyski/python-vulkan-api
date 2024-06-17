import ctypes, sys

class VkCopyAccelerationStructureToMemoryInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyAccelerationStructureToMemoryInfoKHR

from . import VkDeviceOrHostAddressKHR

VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]
