from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSampleLocationsInfoEXT'
_member_list_ = ['sType', 'pNext', 'sampleLocationsPerPixel', 'sampleLocationGridSize', 'sampleLocationsCount', 'pSampleLocations']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sampleLocationsPerPixel': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSampleCountFlagBits',
        'is_string': False,
    },
    'sampleLocationGridSize': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'sampleLocationsCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSampleLocations': {
        'type': CPointerType(CComplexType('VkSampleLocationEXT')),
        'type_name': 'VkSampleLocationEXT',
        'structure': 'VkSampleLocationEXT',
        'length': [['sampleLocationsCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkImageMemoryBarrier',
    'VkImageMemoryBarrier2',
}
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
    'VkSampleLocationEXT',
}
_included_in_ = {
    'VkAttachmentSampleLocationsEXT',
    'VkPipelineSampleLocationsStateCreateInfoEXT',
    'VkSubpassSampleLocationsEXT',
}
_input_of_ = {
    'vkCmdSetSampleLocationsEXT',
}
_output_of_ = set()
