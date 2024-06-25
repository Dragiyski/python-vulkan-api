import ctypes

class VkPhysicalDeviceMemoryProperties2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'memoryProperties': VkPhysicalDeviceMemoryProperties,
        }


from .VkPhysicalDeviceMemoryProperties import VkPhysicalDeviceMemoryProperties

VkPhysicalDeviceMemoryProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]
