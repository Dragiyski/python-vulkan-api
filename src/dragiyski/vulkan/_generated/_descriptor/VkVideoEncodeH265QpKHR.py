from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265QpKHR'
_member_list_ = ['qpI', 'qpP', 'qpB']
_member_info_ = {
    'qpI': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'qpP': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'qpB': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkVideoEncodeH265QualityLevelPropertiesKHR',
    'VkVideoEncodeH265RateControlLayerInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
