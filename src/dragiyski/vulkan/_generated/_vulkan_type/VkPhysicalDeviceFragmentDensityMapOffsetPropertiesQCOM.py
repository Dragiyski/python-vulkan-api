import ctypes

class VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetGranularity', VkExtent2D),
]

VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityOffsetGranularity': VkExtent2D,
}
