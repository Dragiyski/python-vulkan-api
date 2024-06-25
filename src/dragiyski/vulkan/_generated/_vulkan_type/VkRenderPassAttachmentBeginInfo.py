import ctypes

class VkRenderPassAttachmentBeginInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
    ]

VkRenderPassAttachmentBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentCount': ctypes.c_uint32,
    'pAttachments': ctypes.POINTER(ctypes.c_void_p),
}
