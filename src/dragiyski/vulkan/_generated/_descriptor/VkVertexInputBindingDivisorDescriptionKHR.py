from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVertexInputBindingDivisorDescriptionKHR'
_member_list_ = ['binding', 'divisor']
_member_info_ = {
    'binding': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'divisor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineVertexInputDivisorStateCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
