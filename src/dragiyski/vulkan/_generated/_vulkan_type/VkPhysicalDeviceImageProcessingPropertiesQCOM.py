import ctypes

class VkPhysicalDeviceImageProcessingPropertiesQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkPhysicalDeviceImageProcessingPropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxWeightFilterPhases', ctypes.c_uint32),
    ('maxWeightFilterDimension', VkExtent2D),
    ('maxBlockMatchRegion', VkExtent2D),
    ('maxBoxFilterBlockSize', VkExtent2D),
]

VkPhysicalDeviceImageProcessingPropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxWeightFilterPhases': ctypes.c_uint32,
    'maxWeightFilterDimension': VkExtent2D,
    'maxBlockMatchRegion': VkExtent2D,
    'maxBoxFilterBlockSize': VkExtent2D,
}
