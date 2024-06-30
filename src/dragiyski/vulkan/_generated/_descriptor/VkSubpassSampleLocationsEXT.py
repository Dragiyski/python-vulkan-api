from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassSampleLocationsEXT'
_member_list_ = ['subpassIndex', 'sampleLocationsInfo']
_member_info_ = {
    'subpassIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sampleLocationsInfo': {
        'type': CComplexType('VkSampleLocationsInfoEXT'),
        'type_name': 'VkSampleLocationsInfoEXT',
        'structure': 'VkSampleLocationsInfoEXT',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkSampleLocationsInfoEXT',
}
_included_in_ = {
    'VkRenderPassSampleLocationsBeginInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
