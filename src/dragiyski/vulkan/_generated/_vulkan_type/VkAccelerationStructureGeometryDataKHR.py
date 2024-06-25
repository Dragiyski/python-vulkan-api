import ctypes

class VkAccelerationStructureGeometryDataKHR(ctypes.Union):
    pass

from .VkAccelerationStructureGeometryAabbsDataKHR import VkAccelerationStructureGeometryAabbsDataKHR
from .VkAccelerationStructureGeometryInstancesDataKHR import VkAccelerationStructureGeometryInstancesDataKHR
from .VkAccelerationStructureGeometryTrianglesDataKHR import VkAccelerationStructureGeometryTrianglesDataKHR

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]

VkAccelerationStructureGeometryDataKHR._type_ = {
    'triangles': VkAccelerationStructureGeometryTrianglesDataKHR,
    'aabbs': VkAccelerationStructureGeometryAabbsDataKHR,
    'instances': VkAccelerationStructureGeometryInstancesDataKHR,
}
