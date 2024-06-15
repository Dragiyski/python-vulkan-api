import ctypes, sys

class VkAccelerationStructureGeometryMotionTrianglesDataNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkAccelerationStructureGeometryMotionTrianglesDataNV

from . import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryMotionTrianglesDataNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
]
