import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('display', ctypes.c_void_p),
    ('displayName', ctypes.c_char_p),
    ('physicalDimensions', VkExtent2D),
    ('physicalResolution', VkExtent2D),
    ('supportedTransforms', ctypes.c_uint32),
    ('planeReorderPossible', ctypes.c_uint32),
    ('persistentContent', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': {
        'VkDisplayProperties2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceDisplayPropertiesKHR',
    },
    'member_map': {
        'display': {'python_name': ['display']},
        'displayName': {'python_name': ['display', 'name'], 'len': [['null-terminated']]},
        'physicalDimensions': {'python_name': ['physical', 'dimensions'], 'type': 'VkExtent2D'},
        'physicalResolution': {'python_name': ['physical', 'resolution'], 'type': 'VkExtent2D'},
        'supportedTransforms': {'python_name': ['supported', 'transforms'], 'type': 'VkSurfaceTransformFlagsKHR'},
        'planeReorderPossible': {'python_name': ['plane', 'reorder', 'possible']},
        'persistentContent': {'python_name': ['persistent', 'content']},
    }
}
