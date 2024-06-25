import ctypes

class VkDeviceImageMemoryRequirements(ctypes.Structure):
    pass

from .VkImageCreateInfo import VkImageCreateInfo

VkDeviceImageMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('planeAspect', ctypes.c_uint32),
]

VkDeviceImageMemoryRequirements._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pCreateInfo': ctypes.POINTER(VkImageCreateInfo),
    'planeAspect': ctypes.c_uint32,
}
