import ctypes

class VkDeviceBufferMemoryRequirements(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pCreateInfo': ctypes.POINTER(VkBufferCreateInfo),
        }


from .VkBufferCreateInfo import VkBufferCreateInfo

VkDeviceBufferMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]
