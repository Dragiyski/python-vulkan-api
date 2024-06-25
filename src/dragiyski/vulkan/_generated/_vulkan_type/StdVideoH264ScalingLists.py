import ctypes

class StdVideoH264ScalingLists(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'scaling_list_present_mask': ctypes.c_uint16,
            'use_default_scaling_matrix_mask': ctypes.c_uint16,
            'ScalingList4x4': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6),
            'ScalingList8x8': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6),
        }

    _fields_ = [
        ('scaling_list_present_mask', ctypes.c_uint16),
        ('use_default_scaling_matrix_mask', ctypes.c_uint16),
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
    ]
