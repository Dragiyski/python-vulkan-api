import ctypes

class VkAccelerationStructureGeometryAabbsDataKHR(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkAccelerationStructureGeometryAabbsDataKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('data', VkDeviceOrHostAddressConstKHR),
    ('stride', ctypes.c_uint64),
]

VkAccelerationStructureGeometryAabbsDataKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'data': VkDeviceOrHostAddressConstKHR,
    'stride': ctypes.c_uint64,
}
