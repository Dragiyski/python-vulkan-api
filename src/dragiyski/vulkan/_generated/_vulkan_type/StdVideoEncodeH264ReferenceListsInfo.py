import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264RefListModEntry import CType as StdVideoEncodeH264RefListModEntry
from .StdVideoEncodeH264RefPicMarkingEntry import CType as StdVideoEncodeH264RefPicMarkingEntry
from .StdVideoEncodeH264ReferenceListsInfoFlags import CType as StdVideoEncodeH264ReferenceListsInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('refList0ModOpCount', ctypes.c_uint8),
    ('refList1ModOpCount', ctypes.c_uint8),
    ('refPicMarkingOpCount', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pRefList0ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefList1ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefPicMarkingOperations', ctypes.POINTER(StdVideoEncodeH264RefPicMarkingEntry)),
]
