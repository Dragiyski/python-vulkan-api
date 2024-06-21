import ctypes

class CType(ctypes.Union):
    pass

from .VkAccelerationStructureGeometryAabbsDataKHR import CType as VkAccelerationStructureGeometryAabbsDataKHR
from .VkAccelerationStructureGeometryInstancesDataKHR import CType as VkAccelerationStructureGeometryInstancesDataKHR
from .VkAccelerationStructureGeometryTrianglesDataKHR import CType as VkAccelerationStructureGeometryTrianglesDataKHR

CType._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]
