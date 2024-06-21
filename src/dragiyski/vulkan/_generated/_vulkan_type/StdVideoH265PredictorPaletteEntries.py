import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]
