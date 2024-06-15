import ctypes, sys

class VkVideoPictureResourceInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoPictureResourceInfoKHR

from . import VkExtent2D
from . import VkOffset2D

VkVideoPictureResourceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('codedOffset', VkOffset2D),
    ('codedExtent', VkExtent2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('imageViewBinding', ctypes.c_void_p),
]
