import ctypes, sys

class VkAccelerationStructureGeometryTrianglesDataKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryTrianglesDataKHR

from . import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryTrianglesDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexFormat', ctypes.c_int),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
    ('vertexStride', ctypes.c_uint64),
    ('maxVertex', ctypes.c_uint32),
    ('indexType', ctypes.c_int),
    ('indexData', VkDeviceOrHostAddressConstKHR),
    ('transformData', VkDeviceOrHostAddressConstKHR),
]
