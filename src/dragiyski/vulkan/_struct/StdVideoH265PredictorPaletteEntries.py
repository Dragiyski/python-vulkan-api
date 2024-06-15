import ctypes, sys

class StdVideoH265PredictorPaletteEntries(ctypes.Structure):
    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]

sys.modules[__name__] = StdVideoH265PredictorPaletteEntries
