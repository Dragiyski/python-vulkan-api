import ctypes

class CType(ctypes.Structure):
    pass

from .VkSampleLocationsInfoEXT import CType as VkSampleLocationsInfoEXT

CType._fields_ = [
    ('attachmentIndex', ctypes.c_uint32),
    ('sampleLocationsInfo', VkSampleLocationsInfoEXT),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkSampleLocationsInfoEXT',
    },
    'included_in': {
        'VkRenderPassSampleLocationsBeginInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'attachmentIndex': {'python_name': ['attachment', 'index']},
        'sampleLocationsInfo': {'python_name': ['sample', 'locations', 'info'], 'type': 'VkSampleLocationsInfoEXT'},
    }
}
