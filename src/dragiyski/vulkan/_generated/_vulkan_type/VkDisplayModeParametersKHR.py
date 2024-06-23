import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': {
        'VkDisplayModeCreateInfoKHR',
        'VkDisplayModePropertiesKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'visibleRegion': {'python_name': ['visible', 'region'], 'type': 'VkExtent2D'},
        'refreshRate': {'python_name': ['refresh', 'rate']},
    }
}
