from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264FrameSizeKHR'
_member_list_ = ['frameISize', 'framePSize', 'frameBSize']
_member_info_ = {
    'frameISize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'framePSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frameBSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkVideoEncodeH264RateControlLayerInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
