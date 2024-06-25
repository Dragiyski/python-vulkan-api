import ctypes

class StdVideoH265ProfileTierLevel(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoH265ProfileTierLevelFlags,
            'general_profile_idc': ctypes.c_int,
            'general_level_idc': ctypes.c_int,
        }


from .StdVideoH265ProfileTierLevelFlags import StdVideoH265ProfileTierLevelFlags

StdVideoH265ProfileTierLevel._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]
