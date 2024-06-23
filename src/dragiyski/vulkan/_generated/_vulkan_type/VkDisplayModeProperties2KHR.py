import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModePropertiesKHR import CType as VkDisplayModePropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayModeProperties', VkDisplayModePropertiesKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayModePropertiesKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDisplayModeProperties2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_MODE_PROPERTIES_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'displayModeProperties': {'python_name': ['display', 'mode', 'properties'], 'type': 'VkDisplayModePropertiesKHR'},
    }
}
