import ctypes, sys

class StdVideoEncodeH264RefListModEntry(ctypes.Structure):
    _fields_ = [
        ('modification_of_pic_nums_idc', ctypes.c_int),
        ('abs_diff_pic_num_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
    ]

sys.modules[__name__] = StdVideoEncodeH264RefListModEntry
