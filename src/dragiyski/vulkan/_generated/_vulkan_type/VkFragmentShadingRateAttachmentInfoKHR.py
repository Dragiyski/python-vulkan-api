import ctypes

class VkFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    pass

from .VkAttachmentReference2 import VkAttachmentReference2
from .VkExtent2D import VkExtent2D

VkFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

VkFragmentShadingRateAttachmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pFragmentShadingRateAttachment': ctypes.POINTER(VkAttachmentReference2),
    'shadingRateAttachmentTexelSize': VkExtent2D,
}
