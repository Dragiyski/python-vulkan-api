import ctypes

class VkValidationFlagsEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'disabledValidationCheckCount': ctypes.c_uint32,
            'pDisabledValidationChecks': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disabledValidationCheckCount', ctypes.c_uint32),
        ('pDisabledValidationChecks', ctypes.POINTER(ctypes.c_int)),
    ]
