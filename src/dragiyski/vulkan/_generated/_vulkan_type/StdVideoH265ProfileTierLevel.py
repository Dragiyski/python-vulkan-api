import ctypes, sys

class StdVideoH265ProfileTierLevel(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoH265ProfileTierLevel

from . import StdVideoH265ProfileTierLevelFlags

StdVideoH265ProfileTierLevel._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]
