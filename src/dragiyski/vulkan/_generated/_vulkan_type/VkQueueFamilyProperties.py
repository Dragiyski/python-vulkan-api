import ctypes

class VkQueueFamilyProperties(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D

VkQueueFamilyProperties._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]

VkQueueFamilyProperties._type_ = {
    'queueFlags': ctypes.c_uint32,
    'queueCount': ctypes.c_uint32,
    'timestampValidBits': ctypes.c_uint32,
    'minImageTransferGranularity': VkExtent3D,
}
