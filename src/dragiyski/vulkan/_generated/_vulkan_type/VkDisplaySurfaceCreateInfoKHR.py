import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('displayMode', ctypes.c_void_p),
    ('planeIndex', ctypes.c_uint32),
    ('planeStackIndex', ctypes.c_uint32),
    ('transform', ctypes.c_uint32),
    ('globalAlpha', ctypes.c_float),
    ('alphaMode', ctypes.c_uint32),
    ('imageExtent', VkExtent2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateDisplayPlaneSurfaceKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDisplaySurfaceCreateFlagsKHR'},
        'displayMode': {'python_name': ['display', 'mode']},
        'planeIndex': {'python_name': ['plane', 'index']},
        'planeStackIndex': {'python_name': ['plane', 'stack', 'index']},
        'transform': {'python_name': ['transform'], 'type': 'VkSurfaceTransformFlagBitsKHR'},
        'globalAlpha': {'python_name': ['global', 'alpha']},
        'alphaMode': {'python_name': ['alpha', 'mode'], 'type': 'VkDisplayPlaneAlphaFlagBitsKHR'},
        'imageExtent': {'python_name': ['image', 'extent'], 'type': 'VkExtent2D'},
    }
}
