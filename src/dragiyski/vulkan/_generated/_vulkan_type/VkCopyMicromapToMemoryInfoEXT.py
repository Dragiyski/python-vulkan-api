import ctypes

class VkCopyMicromapToMemoryInfoEXT(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressKHR import VkDeviceOrHostAddressKHR

VkCopyMicromapToMemoryInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]

VkCopyMicromapToMemoryInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': ctypes.c_void_p,
    'dst': VkDeviceOrHostAddressKHR,
    'mode': ctypes.c_int,
}
