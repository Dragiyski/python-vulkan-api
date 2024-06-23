import ctypes

class CType(ctypes.Structure):
    pass

from .VkCoarseSampleLocationNV import CType as VkCoarseSampleLocationNV

CType._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkCoarseSampleLocationNV',
    },
    'included_in': {
        'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
    },
    'input_of': {
        'vkCmdSetCoarseSampleOrderNV',
    },
    'output_of': set(),
    'member_map': {
        'shadingRate': {'python_name': ['shading', 'rate'], 'type': 'VkShadingRatePaletteEntryNV'},
        'sampleCount': {'python_name': ['sample', 'count']},
        'sampleLocationCount': {'python_name': ['sample', 'location', 'count']},
        'pSampleLocations': {'python_name': ['p', 'sample', 'locations'], 'len': [['sampleLocationCount']], 'type': 'VkCoarseSampleLocationNV'},
    }
}
