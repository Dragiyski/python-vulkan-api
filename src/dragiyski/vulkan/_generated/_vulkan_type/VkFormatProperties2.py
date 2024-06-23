import ctypes

class CType(ctypes.Structure):
    pass

from .VkFormatProperties import CType as VkFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatProperties', VkFormatProperties),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDrmFormatModifierPropertiesList2EXT',
        'VkDrmFormatModifierPropertiesListEXT',
        'VkFormatProperties3',
        'VkSubpassResolvePerformanceQueryEXT',
    },
    'includes': {
        'VkFormatProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceFormatProperties2',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'formatProperties': {'python_name': ['format', 'properties'], 'type': 'VkFormatProperties'},
    }
}
