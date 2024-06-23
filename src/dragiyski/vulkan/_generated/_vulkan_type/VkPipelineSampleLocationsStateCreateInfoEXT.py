import ctypes

class CType(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import CType as VkSampleLocationsInfoEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsEnable', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

descriptor = {
    'extends': {
        'VkPipelineMultisampleStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkSampleLocationsInfoEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_SAMPLE_LOCATIONS_STATE_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sampleLocationsEnable': {'python_name': ['sample', 'locations', 'enable']},
        'sampleLocationsInfo': {'python_name': ['sample', 'locations', 'info'], 'type': 'VkSampleLocationsInfoEXT'},
    }
}
