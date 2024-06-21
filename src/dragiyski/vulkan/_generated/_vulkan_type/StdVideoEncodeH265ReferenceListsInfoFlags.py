import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('ref_pic_list_modification_flag_l0', ctypes.c_uint32, 1),
        ('ref_pic_list_modification_flag_l1', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
