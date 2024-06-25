import ctypes

class VkCopyMemoryToMicromapInfoEXT(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import VkDeviceOrHostAddressConstKHR

VkCopyMemoryToMicromapInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]

VkCopyMemoryToMicromapInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'src': VkDeviceOrHostAddressConstKHR,
    'dst': ctypes.c_void_p,
    'mode': ctypes.c_int,
}
