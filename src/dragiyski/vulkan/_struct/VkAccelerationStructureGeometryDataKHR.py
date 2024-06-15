import ctypes, sys

class VkAccelerationStructureGeometryDataKHR(ctypes.Union):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryDataKHR

from . import VkAccelerationStructureGeometryAabbsDataKHR
from . import VkAccelerationStructureGeometryInstancesDataKHR
from . import VkAccelerationStructureGeometryTrianglesDataKHR

VkAccelerationStructureGeometryDataKHR._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]
