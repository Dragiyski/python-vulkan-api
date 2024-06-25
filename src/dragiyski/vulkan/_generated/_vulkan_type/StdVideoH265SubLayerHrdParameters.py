import ctypes

class StdVideoH265SubLayerHrdParameters(ctypes.Structure):
    _fields_ = [
        ('bit_rate_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('bit_rate_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cbr_flag', ctypes.c_uint32),
    ]

StdVideoH265SubLayerHrdParameters._type_ = {
    'bit_rate_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cpb_size_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cpb_size_du_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'bit_rate_du_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cbr_flag': ctypes.c_uint32,
}
