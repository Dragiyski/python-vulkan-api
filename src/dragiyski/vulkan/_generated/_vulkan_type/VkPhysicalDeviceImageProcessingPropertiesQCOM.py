import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxWeightFilterPhases', ctypes.c_uint32),
    ('maxWeightFilterDimension', VkExtent2D),
    ('maxBlockMatchRegion', VkExtent2D),
    ('maxBoxFilterBlockSize', VkExtent2D),
]
