import ctypes

class VkCopyMemoryToAccelerationStructureInfoKHR(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToAccelerationStructureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]

VkCopyMemoryToAccelerationStructureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': VkDeviceOrHostAddressConstKHR,
    'dst': ctypes.c_void_p,
    'mode': ctypes.c_int,
}
