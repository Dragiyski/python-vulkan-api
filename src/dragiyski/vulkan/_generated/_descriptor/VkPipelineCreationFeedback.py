from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineCreationFeedback'
_member_list_ = ['flags', 'duration']
_member_info_ = {
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCreationFeedbackFlags',
        'enum': 'VkPipelineCreationFeedbackFlags',
        'is_string': False,
    },
    'duration': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineCreationFeedbackCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
