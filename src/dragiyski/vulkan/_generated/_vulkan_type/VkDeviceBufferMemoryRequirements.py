import ctypes

class VkDeviceBufferMemoryRequirements(ctypes.Structure):
    pass

from .VkBufferCreateInfo import VkBufferCreateInfo

VkDeviceBufferMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]

VkDeviceBufferMemoryRequirements._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pCreateInfo': ctypes.POINTER(VkBufferCreateInfo),
}
