from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkViewportWScalingNV'
_member_list_ = ['xcoeff', 'ycoeff']
_member_info_ = {
    'xcoeff': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'ycoeff': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineViewportWScalingStateCreateInfoNV',
}
_input_of_ = {
    'vkCmdSetViewportWScalingNV',
}
_output_of_ = set()
