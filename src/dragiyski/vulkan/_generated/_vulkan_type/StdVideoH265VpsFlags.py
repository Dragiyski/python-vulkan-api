import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('vps_temporal_id_nesting_flag', ctypes.c_uint32, 1),
        ('vps_sub_layer_ordering_info_present_flag', ctypes.c_uint32, 1),
        ('vps_timing_info_present_flag', ctypes.c_uint32, 1),
        ('vps_poc_proportional_to_timing_flag', ctypes.c_uint32, 1),
    ]
