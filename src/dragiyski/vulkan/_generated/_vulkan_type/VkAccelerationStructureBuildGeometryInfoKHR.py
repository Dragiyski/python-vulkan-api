import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureGeometryKHR import CType as VkAccelerationStructureGeometryKHR
from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR

CType._fields_ = [
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
