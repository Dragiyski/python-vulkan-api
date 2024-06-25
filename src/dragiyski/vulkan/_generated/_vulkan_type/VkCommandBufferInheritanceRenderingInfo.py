import ctypes

class VkCommandBufferInheritanceRenderingInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'viewMask': ctypes.c_uint32,
            'colorAttachmentCount': ctypes.c_uint32,
            'pColorAttachmentFormats': ctypes.POINTER(ctypes.c_int),
            'depthAttachmentFormat': ctypes.c_int,
            'stencilAttachmentFormat': ctypes.c_int,
            'rasterizationSamples': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('viewMask', ctypes.c_uint32),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentFormats', ctypes.POINTER(ctypes.c_int)),
        ('depthAttachmentFormat', ctypes.c_int),
        ('stencilAttachmentFormat', ctypes.c_int),
        ('rasterizationSamples', ctypes.c_uint32),
    ]
