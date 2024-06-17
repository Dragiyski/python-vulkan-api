import ctypes, sys

class StdVideoDecodeAV1ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

sys.modules[__name__] = StdVideoDecodeAV1ReferenceInfoFlags
