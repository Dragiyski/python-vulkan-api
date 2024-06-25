import ctypes

class VkQueueFamilyProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'queueFlags': ctypes.c_uint32,
            'queueCount': ctypes.c_uint32,
            'timestampValidBits': ctypes.c_uint32,
            'minImageTransferGranularity': VkExtent3D,
        }


from .VkExtent3D import VkExtent3D

VkQueueFamilyProperties._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]
