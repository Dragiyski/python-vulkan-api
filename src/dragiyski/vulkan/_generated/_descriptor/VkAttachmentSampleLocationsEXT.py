from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAttachmentSampleLocationsEXT'
_member_list_ = ['attachmentIndex', 'sampleLocationsInfo']
_member_info_ = {
    'attachmentIndex': {
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
