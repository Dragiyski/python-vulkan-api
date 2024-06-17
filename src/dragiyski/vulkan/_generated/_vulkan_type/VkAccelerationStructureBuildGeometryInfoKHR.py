import ctypes, sys

class VkAccelerationStructureBuildGeometryInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureBuildGeometryInfoKHR

from . import VkAccelerationStructureGeometryKHR
from . import VkDeviceOrHostAddressKHR

VkAccelerationStructureBuildGeometryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('mode', ctypes.c_int),
    ('srcAccelerationStructure', ctypes.c_void_p),
    ('dstAccelerationStructure', ctypes.c_void_p),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkAccelerationStructureGeometryKHR)),
    ('ppGeometries', ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureGeometryKHR))),
    ('scratchData', VkDeviceOrHostAddressKHR),
]
