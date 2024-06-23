import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import CType as VkDisplayModeParametersKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('parameters', VkDisplayModeParametersKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayModeParametersKHR',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateDisplayModeKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DISPLAY_MODE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDisplayModeCreateFlagsKHR'},
        'parameters': {'python_name': ['parameters'], 'type': 'VkDisplayModeParametersKHR'},
    }
}
