import ctypes

class VkAttachmentReference(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'attachment': ctypes.c_uint32,
            'layout': ctypes.c_int,
        }

    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]
