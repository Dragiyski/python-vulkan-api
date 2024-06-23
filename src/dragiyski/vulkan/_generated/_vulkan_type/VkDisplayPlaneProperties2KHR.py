import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPlanePropertiesKHR import CType as VkDisplayPlanePropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPlaneProperties', VkDisplayPlanePropertiesKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayPlanePropertiesKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceDisplayPlaneProperties2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_PROPERTIES_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'displayPlaneProperties': {'python_name': ['display', 'plane', 'properties'], 'type': 'VkDisplayPlanePropertiesKHR'},
    }
}
