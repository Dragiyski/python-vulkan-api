import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265ProfileTierLevelFlags import CType as StdVideoH265ProfileTierLevelFlags

CType._fields_ = [
    ('flags', StdVideoH265ProfileTierLevelFlags),
    ('general_profile_idc', ctypes.c_int),
    ('general_level_idc', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265ProfileTierLevelFlags',
    },
    'included_in': {
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265ProfileTierLevelFlags'},
        'general_profile_idc': {'python_name': ['general', 'profile', 'idc'], 'type': 'StdVideoH265ProfileIdc'},
        'general_level_idc': {'python_name': ['general', 'level', 'idc'], 'type': 'StdVideoH265LevelIdc'},
    }
}
