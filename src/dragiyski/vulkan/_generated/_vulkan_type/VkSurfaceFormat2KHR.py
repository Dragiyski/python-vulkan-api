import ctypes

class CType(ctypes.Structure):
    pass

from .VkSurfaceFormatKHR import CType as VkSurfaceFormatKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkImageCompressionPropertiesEXT',
    },
    'includes': {
        'VkSurfaceFormatKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSurfaceFormats2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SURFACE_FORMAT_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'surfaceFormat': {'python_name': ['surface', 'format'], 'type': 'VkSurfaceFormatKHR'},
    }
}
