import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minImageCount', ctypes.c_uint32),
    ('maxImageCount', ctypes.c_uint32),
    ('currentExtent', VkExtent2D),
    ('minImageExtent', VkExtent2D),
    ('maxImageExtent', VkExtent2D),
    ('maxImageArrayLayers', ctypes.c_uint32),
    ('supportedTransforms', ctypes.c_uint32),
    ('currentTransform', ctypes.c_uint32),
    ('supportedCompositeAlpha', ctypes.c_uint32),
    ('supportedUsageFlags', ctypes.c_uint32),
    ('supportedSurfaceCounters', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSurfaceCapabilities2EXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'minImageCount': {'python_name': ['min', 'image', 'count']},
        'maxImageCount': {'python_name': ['max', 'image', 'count']},
        'currentExtent': {'python_name': ['current', 'extent'], 'type': 'VkExtent2D'},
        'minImageExtent': {'python_name': ['min', 'image', 'extent'], 'type': 'VkExtent2D'},
        'maxImageExtent': {'python_name': ['max', 'image', 'extent'], 'type': 'VkExtent2D'},
        'maxImageArrayLayers': {'python_name': ['max', 'image', 'array', 'layers']},
        'supportedTransforms': {'python_name': ['supported', 'transforms'], 'type': 'VkSurfaceTransformFlagsKHR'},
        'currentTransform': {'python_name': ['current', 'transform'], 'type': 'VkSurfaceTransformFlagBitsKHR'},
        'supportedCompositeAlpha': {'python_name': ['supported', 'composite', 'alpha'], 'type': 'VkCompositeAlphaFlagsKHR'},
        'supportedUsageFlags': {'python_name': ['supported', 'usage', 'flags'], 'type': 'VkImageUsageFlags'},
        'supportedSurfaceCounters': {'python_name': ['supported', 'surface', 'counters'], 'type': 'VkSurfaceCounterFlagsEXT'},
    }
}
