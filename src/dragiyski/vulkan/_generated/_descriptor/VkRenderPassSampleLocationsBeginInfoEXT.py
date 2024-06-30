from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassSampleLocationsBeginInfoEXT'
_member_list_ = ['sType', 'pNext', 'attachmentInitialSampleLocationsCount', 'pAttachmentInitialSampleLocations', 'postSubpassSampleLocationsCount', 'pPostSubpassSampleLocations']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_SAMPLE_LOCATIONS_BEGIN_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'attachmentInitialSampleLocationsCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pAttachmentInitialSampleLocations': {
        'type': CPointerType(CComplexType('VkAttachmentSampleLocationsEXT')),
        'type_name': 'VkAttachmentSampleLocationsEXT',
        'structure': 'VkAttachmentSampleLocationsEXT',
        'length': [['attachmentInitialSampleLocationsCount']],
        'is_string': False,
    },
    'postSubpassSampleLocationsCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPostSubpassSampleLocations': {
        'type': CPointerType(CComplexType('VkSubpassSampleLocationsEXT')),
        'type_name': 'VkSubpassSampleLocationsEXT',
        'structure': 'VkSubpassSampleLocationsEXT',
        'length': [['postSubpassSampleLocationsCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassBeginInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkAttachmentSampleLocationsEXT',
    'VkSubpassSampleLocationsEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
