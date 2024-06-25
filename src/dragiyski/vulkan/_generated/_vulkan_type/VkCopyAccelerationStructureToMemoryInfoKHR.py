import ctypes

class VkCopyAccelerationStructureToMemoryInfoKHR(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkCopyAccelerationStructureToMemoryInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]

VkCopyAccelerationStructureToMemoryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': ctypes.c_void_p,
    'dst': VkDeviceOrHostAddressKHR,
    'mode': ctypes.c_int,
}
