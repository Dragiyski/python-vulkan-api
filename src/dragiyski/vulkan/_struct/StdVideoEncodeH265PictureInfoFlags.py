import ctypes, sys

class StdVideoEncodeH265PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('is_reference', ctypes.c_uint32, 1),
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('discardable_flag', ctypes.c_uint32, 1),
        ('cross_layer_bla_flag', ctypes.c_uint32, 1),
        ('pic_output_flag', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
        ('slice_temporal_mvp_enabled_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 23),
    ]

sys.modules[__name__] = StdVideoEncodeH265PictureInfoFlags
