import ctypes, sys

class VkRenderingAttachmentInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderingAttachmentInfo

from . import VkClearValue

VkRenderingAttachmentInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('resolveMode', ctypes.c_uint32),
    ('resolveImageView', ctypes.c_void_p),
    ('resolveImageLayout', ctypes.c_int),
    ('loadOp', ctypes.c_int),
    ('storeOp', ctypes.c_int),
    ('clearValue', VkClearValue),
]
