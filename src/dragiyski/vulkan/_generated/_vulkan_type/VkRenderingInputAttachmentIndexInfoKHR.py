import ctypes

class VkRenderingInputAttachmentIndexInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'colorAttachmentCount': ctypes.c_uint32,
            'pColorAttachmentInputIndices': ctypes.POINTER(ctypes.c_uint32),
            'pDepthInputAttachmentIndex': ctypes.POINTER(ctypes.c_uint32),
            'pStencilInputAttachmentIndex': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentInputIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pDepthInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
        ('pStencilInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
    ]
