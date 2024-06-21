import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrderColorAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderDepthAttachmentAccess', ctypes.c_uint32),
        ('rasterizationOrderStencilAttachmentAccess', ctypes.c_uint32),
    ]
