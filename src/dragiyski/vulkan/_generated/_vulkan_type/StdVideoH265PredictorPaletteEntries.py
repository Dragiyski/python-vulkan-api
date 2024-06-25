import ctypes

class StdVideoH265PredictorPaletteEntries(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'PredictorPaletteEntries': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3),
        }

    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]
