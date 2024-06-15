import ctypes, sys

class VkAccelerationStructureGeometryAabbsDataKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryAabbsDataKHR

from . import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryAabbsDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('stride', ctypes.c_uint64),
]
