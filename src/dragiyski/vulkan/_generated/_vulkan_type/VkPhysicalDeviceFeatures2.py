import ctypes

class VkPhysicalDeviceFeatures2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'features': VkPhysicalDeviceFeatures,
        }


from .VkPhysicalDeviceFeatures import VkPhysicalDeviceFeatures

VkPhysicalDeviceFeatures2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('features', VkPhysicalDeviceFeatures),
]
