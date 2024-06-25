import ctypes

class StdVideoAV1Segmentation(ctypes.Structure):
    _fields_ = [
        ('FeatureEnabled', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('FeatureData', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8)),
    ]

StdVideoAV1Segmentation._type_ = {
    'FeatureEnabled': ctypes.ARRAY(ctypes.c_uint8, 8),
    'FeatureData': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8),
}
