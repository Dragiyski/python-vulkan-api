import ctypes

class VkPhysicalDeviceFeatures2(ctypes.Structure):
    pass

from .VkPhysicalDeviceFeatures import VkPhysicalDeviceFeatures

VkPhysicalDeviceFeatures2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('features', VkPhysicalDeviceFeatures),
]

VkPhysicalDeviceFeatures2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'features': VkPhysicalDeviceFeatures,
}
