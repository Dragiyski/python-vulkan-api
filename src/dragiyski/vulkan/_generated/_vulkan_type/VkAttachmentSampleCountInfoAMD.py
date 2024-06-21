import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentSamples', ctypes.POINTER(ctypes.c_uint32)),
        ('depthStencilAttachmentSamples', ctypes.c_uint32),
    ]
