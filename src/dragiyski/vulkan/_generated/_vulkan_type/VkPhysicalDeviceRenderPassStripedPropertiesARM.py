import ctypes, sys

class VkPhysicalDeviceRenderPassStripedPropertiesARM(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceRenderPassStripedPropertiesARM

from . import VkExtent2D

VkPhysicalDeviceRenderPassStripedPropertiesARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
]
