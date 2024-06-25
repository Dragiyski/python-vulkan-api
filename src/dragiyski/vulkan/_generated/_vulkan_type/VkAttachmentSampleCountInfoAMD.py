import ctypes

class VkAttachmentSampleCountInfoAMD(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'colorAttachmentCount': ctypes.c_uint32,
            'pColorAttachmentSamples': ctypes.POINTER(ctypes.c_uint32),
            'depthStencilAttachmentSamples': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentSamples', ctypes.POINTER(ctypes.c_uint32)),
        ('depthStencilAttachmentSamples', ctypes.c_uint32),
    ]
