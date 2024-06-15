import ctypes, sys

class StdVideoEncodeH265ReferenceListsInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoEncodeH265ReferenceListsInfo

from . import StdVideoEncodeH265ReferenceListsInfoFlags

StdVideoEncodeH265ReferenceListsInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l1', ctypes.ARRAY(ctypes.c_uint8, 15)),
]
