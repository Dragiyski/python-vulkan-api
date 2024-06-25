import ctypes

class VkAttachmentReference(ctypes.Structure):
    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]

VkAttachmentReference._type_ = {
    'attachment': ctypes.c_uint32,
    'layout': ctypes.c_int,
}
