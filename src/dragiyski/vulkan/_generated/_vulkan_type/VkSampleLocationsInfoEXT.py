import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkSampleLocationEXT import CType as VkSampleLocationEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsPerPixel', ctypes.c_uint32),
    ('sampleLocationGridSize', VkExtent2D),
    ('sampleLocationsCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT)),
]

descriptor = {
    'extends': {
        'VkImageMemoryBarrier',
        'VkImageMemoryBarrier2',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkSampleLocationEXT',
    },
    'included_in': {
        'VkAttachmentSampleLocationsEXT',
        'VkPipelineSampleLocationsStateCreateInfoEXT',
        'VkSubpassSampleLocationsEXT',
    },
    'input_of': {
        'vkCmdSetSampleLocationsEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLE_LOCATIONS_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sampleLocationsPerPixel': {'python_name': ['sample', 'locations', 'per', 'pixel'], 'type': 'VkSampleCountFlagBits'},
        'sampleLocationGridSize': {'python_name': ['sample', 'location', 'grid', 'size'], 'type': 'VkExtent2D'},
        'sampleLocationsCount': {'python_name': ['sample', 'locations', 'count']},
        'pSampleLocations': {'python_name': ['p', 'sample', 'locations'], 'len': [['sampleLocationsCount']], 'type': 'VkSampleLocationEXT'},
    }
}
