import ctypes, sys

class VkFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkFragmentShadingRateAttachmentInfoKHR

from . import VkExtent2D
from . import VkAttachmentReference2

VkFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]
