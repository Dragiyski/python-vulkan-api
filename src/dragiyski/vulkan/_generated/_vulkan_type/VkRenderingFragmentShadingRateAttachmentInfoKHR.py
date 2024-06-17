import ctypes, sys

class VkRenderingFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderingFragmentShadingRateAttachmentInfoKHR

from . import VkExtent2D

VkRenderingFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]
