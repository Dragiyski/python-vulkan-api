import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPassStripeGranularity', VkExtent2D),
    ('maxRenderPassStripes', ctypes.c_uint32),
]
