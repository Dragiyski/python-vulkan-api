import ctypes

class VkPhysicalDeviceRenderPassStripedPropertiesARM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceRenderPassStripedPropertiesARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
]

VkPhysicalDeviceRenderPassStripedPropertiesARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPassStripeGranularity': VkExtent2D,
    'maxRenderPassStripes': ctypes.c_uint32,
}
