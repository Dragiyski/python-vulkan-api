import ctypes

class VkAccelerationStructureGeometryTrianglesDataKHR(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

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

VkAccelerationStructureGeometryTrianglesDataKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vertexFormat': ctypes.c_int,
    'vertexData': VkDeviceOrHostAddressConstKHR,
    'vertexStride': ctypes.c_uint64,
    'maxVertex': ctypes.c_uint32,
    'indexType': ctypes.c_int,
    'indexData': VkDeviceOrHostAddressConstKHR,
    'transformData': VkDeviceOrHostAddressConstKHR,
}
