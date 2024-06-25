import ctypes

class VkRenderPassSubpassFeedbackInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'subpassMergeStatus': ctypes.c_int,
            'description': ctypes.ARRAY(ctypes.c_char, 256),
            'postMergeIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('subpassMergeStatus', ctypes.c_int),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('postMergeIndex', ctypes.c_uint32),
    ]
