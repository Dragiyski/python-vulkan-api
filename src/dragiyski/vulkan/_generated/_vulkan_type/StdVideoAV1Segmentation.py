import ctypes

class StdVideoAV1Segmentation(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'FeatureEnabled': ctypes.ARRAY(ctypes.c_uint8, 8),
            'FeatureData': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8),
        }

    _fields_ = [
        ('FeatureEnabled', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('FeatureData', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8)),
    ]
