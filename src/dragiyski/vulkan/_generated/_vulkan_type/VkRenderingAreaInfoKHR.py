import ctypes, sys

class VkRenderingAreaInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewMask', ctypes.c_uint32),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentFormats', ctypes.POINTER(ctypes.c_int)),
        ('depthAttachmentFormat', ctypes.c_int),
        ('stencilAttachmentFormat', ctypes.c_int),
    ]

sys.modules[__name__] = VkRenderingAreaInfoKHR
