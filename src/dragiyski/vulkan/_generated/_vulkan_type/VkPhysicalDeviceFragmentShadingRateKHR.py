import ctypes

class VkPhysicalDeviceFragmentShadingRateKHR(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleCounts', ctypes.c_uint32),
    ('fragmentSize', VkExtent2D),
]

VkPhysicalDeviceFragmentShadingRateKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleCounts': ctypes.c_uint32,
    'fragmentSize': VkExtent2D,
}
