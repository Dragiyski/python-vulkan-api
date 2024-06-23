import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('supportedAlpha', ctypes.c_uint32),
    ('minSrcPosition', VkOffset2D),
    ('maxSrcPosition', VkOffset2D),
    ('minSrcExtent', VkExtent2D),
    ('maxSrcExtent', VkExtent2D),
    ('minDstPosition', VkOffset2D),
    ('maxDstPosition', VkOffset2D),
    ('minDstExtent', VkExtent2D),
    ('maxDstExtent', VkExtent2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkOffset2D',
    },
    'included_in': {
        'VkDisplayPlaneCapabilities2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetDisplayPlaneCapabilitiesKHR',
    },
    'member_map': {
        'supportedAlpha': {'python_name': ['supported', 'alpha'], 'type': 'VkDisplayPlaneAlphaFlagsKHR'},
        'minSrcPosition': {'python_name': ['min', 'src', 'position'], 'type': 'VkOffset2D'},
        'maxSrcPosition': {'python_name': ['max', 'src', 'position'], 'type': 'VkOffset2D'},
        'minSrcExtent': {'python_name': ['min', 'src', 'extent'], 'type': 'VkExtent2D'},
        'maxSrcExtent': {'python_name': ['max', 'src', 'extent'], 'type': 'VkExtent2D'},
        'minDstPosition': {'python_name': ['min', 'dst', 'position'], 'type': 'VkOffset2D'},
        'maxDstPosition': {'python_name': ['max', 'dst', 'position'], 'type': 'VkOffset2D'},
        'minDstExtent': {'python_name': ['min', 'dst', 'extent'], 'type': 'VkExtent2D'},
        'maxDstExtent': {'python_name': ['max', 'dst', 'extent'], 'type': 'VkExtent2D'},
    }
}
