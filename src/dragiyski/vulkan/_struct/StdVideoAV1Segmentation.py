import ctypes, sys

class StdVideoAV1Segmentation(ctypes.Structure):
    _fields_ = [
        ('FeatureEnabled', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('FeatureData', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8)),
    ]

sys.modules[__name__] = StdVideoAV1Segmentation
