import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import CType as VkDisplayModeParametersKHR

CType._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDisplayModeParametersKHR',
    },
    'included_in': {
        'VkDisplayModeProperties2KHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetDisplayModePropertiesKHR',
    },
    'member_map': {
        'displayMode': {'python_name': ['display', 'mode']},
        'parameters': {'python_name': ['parameters'], 'type': 'VkDisplayModeParametersKHR'},
    }
}
