import ctypes

class VkValidationFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'enabledValidationFeatureCount': ctypes.c_uint32,
            'pEnabledValidationFeatures': ctypes.POINTER(ctypes.c_int),
            'disabledValidationFeatureCount': ctypes.c_uint32,
            'pDisabledValidationFeatures': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enabledValidationFeatureCount', ctypes.c_uint32),
        ('pEnabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
        ('disabledValidationFeatureCount', ctypes.c_uint32),
        ('pDisabledValidationFeatures', ctypes.POINTER(ctypes.c_int)),
    ]
