import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('scaling_list_present_mask', ctypes.c_uint16),
        ('use_default_scaling_matrix_mask', ctypes.c_uint16),
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
    ]
