import ctypes

class VkRenderPassCreationFeedbackInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'postMergeSubpassCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]
