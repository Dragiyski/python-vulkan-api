import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('subpass', ctypes.c_uint32),
        ('inputAttachmentIndex', ctypes.c_uint32),
        ('aspectMask', ctypes.c_uint32),
    ]
