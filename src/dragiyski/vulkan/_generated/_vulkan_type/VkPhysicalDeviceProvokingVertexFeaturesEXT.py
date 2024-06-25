import ctypes

class VkPhysicalDeviceProvokingVertexFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'provokingVertexLast': ctypes.c_uint32,
            'transformFeedbackPreservesProvokingVertex': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('provokingVertexLast', ctypes.c_uint32),
        ('transformFeedbackPreservesProvokingVertex', ctypes.c_uint32),
    ]
