from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265ProfileTierLevel'
_member_list_ = ['flags', 'general_profile_idc', 'general_level_idc']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265ProfileTierLevelFlags'),
        'type_name': 'StdVideoH265ProfileTierLevelFlags',
        'structure': 'StdVideoH265ProfileTierLevelFlags',
        'is_string': False,
    },
    'general_profile_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265ProfileIdc',
        'enum': 'StdVideoH265ProfileIdc',
        'is_string': False,
    },
    'general_level_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265LevelIdc',
        'enum': 'StdVideoH265LevelIdc',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH265ProfileTierLevelFlags',
}
_included_in_ = {
    'StdVideoH265SequenceParameterSet',
    'StdVideoH265VideoParameterSet',
}
_input_of_ = set()
_output_of_ = set()
