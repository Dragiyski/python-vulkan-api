import ctypes

class VkAccelerationStructureGeometryDataKHR(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'triangles': VkAccelerationStructureGeometryTrianglesDataKHR,
            'aabbs': VkAccelerationStructureGeometryAabbsDataKHR,
            'instances': VkAccelerationStructureGeometryInstancesDataKHR,
        }


from .VkAccelerationStructureGeometryAabbsDataKHR import VkAccelerationStructureGeometryAabbsDataKHR
from .VkAccelerationStructureGeometryInstancesDataKHR import VkAccelerationStructureGeometryInstancesDataKHR
from .VkAccelerationStructureGeometryTrianglesDataKHR import VkAccelerationStructureGeometryTrianglesDataKHR

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]
