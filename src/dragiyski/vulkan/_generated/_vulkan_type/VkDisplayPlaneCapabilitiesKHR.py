import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('supportedAlpha', ctypes.c_uint32),
    ('minSrcPosition', VkOffset2D),
    ('maxSrcPosition', VkOffset2D),
    ('minSrcExtent', VkExtent2D),
    ('maxSrcExtent', VkExtent2D),
    ('minDstPosition', VkOffset2D),
    ('maxDstPosition', VkOffset2D),
    ('minDstExtent', VkExtent2D),
    ('maxDstExtent', VkExtent2D),
]
