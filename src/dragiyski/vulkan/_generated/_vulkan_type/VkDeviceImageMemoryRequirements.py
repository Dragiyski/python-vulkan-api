import ctypes

class VkDeviceImageMemoryRequirements(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pCreateInfo': ctypes.POINTER(VkImageCreateInfo),
            'planeAspect': ctypes.c_uint32,
        }


from .VkImageCreateInfo import VkImageCreateInfo

VkDeviceImageMemoryRequirements._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('planeAspect', ctypes.c_uint32),
]
