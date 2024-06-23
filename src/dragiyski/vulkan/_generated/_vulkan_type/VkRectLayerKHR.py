import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
    ('layer', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkOffset2D',
    },
    'included_in': {
        'VkPresentRegionKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'offset': {'python_name': ['offset'], 'type': 'VkOffset2D'},
        'extent': {'python_name': ['extent'], 'type': 'VkExtent2D'},
        'layer': {'python_name': ['layer']},
    }
}
