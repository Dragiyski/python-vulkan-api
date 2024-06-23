import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationSampleCounts', ctypes.c_uint32),
    ('maxSampleLocationGridSize', VkExtent2D),
    ('sampleLocationCoordinateRange', ctypes.ARRAY(ctypes.c_float, 2)),
    ('sampleLocationSubPixelBits', ctypes.c_uint32),
    ('variableSampleLocations', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SAMPLE_LOCATIONS_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sampleLocationSampleCounts': {'python_name': ['sample', 'location', 'sample', 'counts'], 'type': 'VkSampleCountFlags'},
        'maxSampleLocationGridSize': {'python_name': ['max', 'sample', 'location', 'grid', 'size'], 'type': 'VkExtent2D'},
        'sampleLocationCoordinateRange': {'python_name': ['sample', 'location', 'coordinate', 'range']},
        'sampleLocationSubPixelBits': {'python_name': ['sample', 'location', 'sub', 'pixel', 'bits']},
        'variableSampleLocations': {'python_name': ['variable', 'sample', 'locations']},
    }
}
