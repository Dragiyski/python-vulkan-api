import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPropertiesKHR import CType as VkDisplayPropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayPropertiesKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceDisplayProperties2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_PROPERTIES_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'displayProperties': {'python_name': ['display', 'properties'], 'type': 'VkDisplayPropertiesKHR'},
    }
}
