import ctypes

class VkInputAttachmentAspectReference(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'subpass': ctypes.c_uint32,
            'inputAttachmentIndex': ctypes.c_uint32,
            'aspectMask': ctypes.c_uint32,
        }

    _fields_ = [
        ('subpass', ctypes.c_uint32),
        ('inputAttachmentIndex', ctypes.c_uint32),
        ('aspectMask', ctypes.c_uint32),
    ]
