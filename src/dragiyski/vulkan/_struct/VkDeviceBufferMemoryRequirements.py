import ctypes, sys

class VkDeviceBufferMemoryRequirements(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceBufferMemoryRequirements

from . import VkBufferCreateInfo

VkDeviceBufferMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]
