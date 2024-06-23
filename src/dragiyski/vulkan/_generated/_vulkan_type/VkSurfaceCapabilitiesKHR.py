import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
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
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': {
        'VkSurfaceCapabilities2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSurfaceCapabilitiesKHR',
    },
    'member_map': {
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
    }
}
