import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('supportedPresentScaling', ctypes.c_uint32),
    ('supportedPresentGravityX', ctypes.c_uint32),
    ('supportedPresentGravityY', ctypes.c_uint32),
    ('minScaledImageExtent', VkExtent2D),
    ('maxScaledImageExtent', VkExtent2D),
]

descriptor = {
    'extends': {
        'VkSurfaceCapabilities2KHR',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SURFACE_PRESENT_SCALING_CAPABILITIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'supportedPresentScaling': {'python_name': ['supported', 'present', 'scaling'], 'type': 'VkPresentScalingFlagsEXT'},
        'supportedPresentGravityX': {'python_name': ['supported', 'present', 'gravity', 'x'], 'type': 'VkPresentGravityFlagsEXT'},
        'supportedPresentGravityY': {'python_name': ['supported', 'present', 'gravity', 'y'], 'type': 'VkPresentGravityFlagsEXT'},
        'minScaledImageExtent': {'python_name': ['min', 'scaled', 'image', 'extent'], 'type': 'VkExtent2D'},
        'maxScaledImageExtent': {'python_name': ['max', 'scaled', 'image', 'extent'], 'type': 'VkExtent2D'},
    }
}
