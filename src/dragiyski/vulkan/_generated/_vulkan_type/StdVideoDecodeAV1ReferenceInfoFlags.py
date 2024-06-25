import ctypes

class StdVideoDecodeAV1ReferenceInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'disable_frame_end_update_cdf': ctypes.c_uint32,
            'segmentation_enabled': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
