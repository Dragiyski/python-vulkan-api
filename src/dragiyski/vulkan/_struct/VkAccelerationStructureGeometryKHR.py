import ctypes, sys

class VkAccelerationStructureGeometryKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryKHR

from . import VkAccelerationStructureGeometryDataKHR

VkAccelerationStructureGeometryKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkAccelerationStructureGeometryDataKHR),
    ('flags', ctypes.c_uint32),
]
