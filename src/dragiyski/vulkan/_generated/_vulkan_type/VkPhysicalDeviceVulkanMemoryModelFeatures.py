import ctypes

class VkPhysicalDeviceVulkanMemoryModelFeatures(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'vulkanMemoryModel': ctypes.c_uint32,
            'vulkanMemoryModelDeviceScope': ctypes.c_uint32,
            'vulkanMemoryModelAvailabilityVisibilityChains': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vulkanMemoryModel', ctypes.c_uint32),
        ('vulkanMemoryModelDeviceScope', ctypes.c_uint32),
        ('vulkanMemoryModelAvailabilityVisibilityChains', ctypes.c_uint32),
    ]
