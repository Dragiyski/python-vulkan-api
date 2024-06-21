import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('still_picture', ctypes.c_uint32, 1),
        ('reduced_still_picture_header', ctypes.c_uint32, 1),
        ('use_128x128_superblock', ctypes.c_uint32, 1),
        ('enable_filter_intra', ctypes.c_uint32, 1),
        ('enable_intra_edge_filter', ctypes.c_uint32, 1),
        ('enable_interintra_compound', ctypes.c_uint32, 1),
        ('enable_masked_compound', ctypes.c_uint32, 1),
        ('enable_warped_motion', ctypes.c_uint32, 1),
        ('enable_dual_filter', ctypes.c_uint32, 1),
        ('enable_order_hint', ctypes.c_uint32, 1),
        ('enable_jnt_comp', ctypes.c_uint32, 1),
        ('enable_ref_frame_mvs', ctypes.c_uint32, 1),
        ('frame_id_numbers_present_flag', ctypes.c_uint32, 1),
        ('enable_superres', ctypes.c_uint32, 1),
        ('enable_cdef', ctypes.c_uint32, 1),
        ('enable_restoration', ctypes.c_uint32, 1),
        ('film_grain_params_present', ctypes.c_uint32, 1),
        ('timing_info_present_flag', ctypes.c_uint32, 1),
        ('initial_display_delay_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 13),
    ]
