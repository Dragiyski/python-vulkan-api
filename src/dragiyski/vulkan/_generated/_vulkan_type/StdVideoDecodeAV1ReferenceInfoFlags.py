import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
