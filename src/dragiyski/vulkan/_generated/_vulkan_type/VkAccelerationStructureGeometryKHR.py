import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureGeometryDataKHR import CType as VkAccelerationStructureGeometryDataKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkAccelerationStructureGeometryDataKHR),
    ('flags', ctypes.c_uint32),
]
