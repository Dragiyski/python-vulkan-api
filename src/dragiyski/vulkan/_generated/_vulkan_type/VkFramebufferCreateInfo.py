import ctypes

class VkFramebufferCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'renderPass': ctypes.c_void_p,
            'attachmentCount': ctypes.c_uint32,
            'pAttachments': ctypes.POINTER(ctypes.c_void_p),
            'width': ctypes.c_uint32,
            'height': ctypes.c_uint32,
            'layers': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('renderPass', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layers', ctypes.c_uint32),
    ]
