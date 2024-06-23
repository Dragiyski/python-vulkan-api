import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearColorValue import CType as VkClearColorValue

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('customBorderColor', VkClearColorValue),
    ('format', ctypes.c_int),
]

descriptor = {
    'extends': {
        'VkSamplerCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkClearColorValue',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_CUSTOM_BORDER_COLOR_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'customBorderColor': {'python_name': ['custom', 'border', 'color'], 'type': 'VkClearColorValue'},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
    }
}
