import ctypes

class VkAccelerationStructureGeometryMotionTrianglesDataNV(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryMotionTrianglesDataNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('vertexData', VkDeviceOrHostAddressConstKHR),
]

VkAccelerationStructureGeometryMotionTrianglesDataNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexData': VkDeviceOrHostAddressConstKHR,
}
