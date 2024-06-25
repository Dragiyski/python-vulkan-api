import ctypes

class StdVideoEncodeH264ReferenceListsInfoFlags(ctypes.Structure):
    _fields_ = [
        ('ref_pic_list_modification_flag_l0', ctypes.c_uint32, 1),
        ('ref_pic_list_modification_flag_l1', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

StdVideoEncodeH264ReferenceListsInfoFlags._type_ = {
    'ref_pic_list_modification_flag_l0': ctypes.c_uint32,
    'ref_pic_list_modification_flag_l1': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
