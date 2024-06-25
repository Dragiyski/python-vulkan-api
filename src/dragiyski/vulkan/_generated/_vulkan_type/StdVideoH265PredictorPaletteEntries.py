import ctypes

class StdVideoH265PredictorPaletteEntries(ctypes.Structure):
    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]

StdVideoH265PredictorPaletteEntries._type_ = {
    'PredictorPaletteEntries': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3),
}
