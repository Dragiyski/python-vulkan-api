import ctypes, sys

class VkAccelerationStructureGeometryDataKHR(ctypes.Union):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryDataKHR

from . import VkAccelerationStructureGeometryInstancesDataKHR
from . import VkAccelerationStructureGeometryTrianglesDataKHR
from . import VkAccelerationStructureGeometryAabbsDataKHR

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]
