from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineSampleLocationsStateCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'sampleLocationsEnable', 'sampleLocationsInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sampleLocationsEnable': {
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
_extends_ = {
    'VkPipelineMultisampleStateCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkSampleLocationsInfoEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
