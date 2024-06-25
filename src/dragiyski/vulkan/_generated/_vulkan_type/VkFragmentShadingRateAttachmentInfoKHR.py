import ctypes

class VkFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pFragmentShadingRateAttachment': ctypes.POINTER(VkAttachmentReference2),
            'shadingRateAttachmentTexelSize': VkExtent2D,
        }


from .VkAttachmentReference2 import VkAttachmentReference2
from .VkExtent2D import VkExtent2D

VkFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]
