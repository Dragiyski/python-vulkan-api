import ctypes

class VkRenderingFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkRenderingFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

VkRenderingFragmentShadingRateAttachmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
    'shadingRateAttachmentTexelSize': VkExtent2D,
}
