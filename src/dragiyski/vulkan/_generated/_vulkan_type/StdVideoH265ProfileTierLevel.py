import ctypes

class StdVideoH265ProfileTierLevel(ctypes.Structure):
    pass

from .StdVideoH265ProfileTierLevelFlags import StdVideoH265ProfileTierLevelFlags

StdVideoH265ProfileTierLevel._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]

StdVideoH265ProfileTierLevel._type_ = {
    'flags': StdVideoH265ProfileTierLevelFlags,
    'general_profile_idc': ctypes.c_int,
    'general_level_idc': ctypes.c_int,
}
