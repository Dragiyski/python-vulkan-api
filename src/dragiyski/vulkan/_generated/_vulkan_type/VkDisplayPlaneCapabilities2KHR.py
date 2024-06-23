import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPlaneCapabilitiesKHR import CType as VkDisplayPlaneCapabilitiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('capabilities', VkDisplayPlaneCapabilitiesKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayPlaneCapabilitiesKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDisplayPlaneCapabilities2KHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_PLANE_CAPABILITIES_2_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'capabilities': {'python_name': ['capabilities'], 'type': 'VkDisplayPlaneCapabilitiesKHR'},
    }
}
