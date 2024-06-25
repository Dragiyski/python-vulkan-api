import ctypes

class StdVideoEncodeH265ReferenceListsInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoEncodeH265ReferenceListsInfoFlags,
            'num_ref_idx_l0_active_minus1': ctypes.c_uint8,
            'num_ref_idx_l1_active_minus1': ctypes.c_uint8,
            'RefPicList0': ctypes.ARRAY(ctypes.c_uint8, 15),
            'RefPicList1': ctypes.ARRAY(ctypes.c_uint8, 15),
            'list_entry_l0': ctypes.ARRAY(ctypes.c_uint8, 15),
            'list_entry_l1': ctypes.ARRAY(ctypes.c_uint8, 15),
        }


from .StdVideoEncodeH265ReferenceListsInfoFlags import StdVideoEncodeH265ReferenceListsInfoFlags

StdVideoEncodeH265ReferenceListsInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l1', ctypes.ARRAY(ctypes.c_uint8, 15)),
]
