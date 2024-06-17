import ctypes, sys

class StdVideoDecodeH265PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('IsReference', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoDecodeH265PictureInfoFlags
