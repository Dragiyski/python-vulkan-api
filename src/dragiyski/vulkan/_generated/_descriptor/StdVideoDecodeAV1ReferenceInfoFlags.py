from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeAV1ReferenceInfoFlags'
_member_list_ = ['disable_frame_end_update_cdf', 'segmentation_enabled', 'reserved']
_member_info_ = {
    'disable_frame_end_update_cdf': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'segmentation_enabled': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 30,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeAV1ReferenceInfo',
}
_input_of_ = set()
_output_of_ = set()
