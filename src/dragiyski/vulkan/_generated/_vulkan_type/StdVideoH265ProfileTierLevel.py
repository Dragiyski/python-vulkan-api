import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265ProfileTierLevelFlags import CType as StdVideoH265ProfileTierLevelFlags

CType._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]
