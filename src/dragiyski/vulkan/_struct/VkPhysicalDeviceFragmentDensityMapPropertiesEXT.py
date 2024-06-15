import ctypes, sys

class VkPhysicalDeviceFragmentDensityMapPropertiesEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceFragmentDensityMapPropertiesEXT

from . import VkExtent2D

VkPhysicalDeviceFragmentDensityMapPropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentDensityTexelSize', VkExtent2D),
    ('maxFragmentDensityTexelSize', VkExtent2D),
    ('fragmentDensityInvocations', ctypes.c_uint32),
]
