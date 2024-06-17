import ctypes, sys

class VkRenderPassAttachmentBeginInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
    ]

sys.modules[__name__] = VkRenderPassAttachmentBeginInfo
