import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('components', VkComponentMapping),
    ('srgb', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkSamplerCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkComponentMapping',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_BORDER_COLOR_COMPONENT_MAPPING_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'components': {'python_name': ['components'], 'type': 'VkComponentMapping'},
        'srgb': {'python_name': ['srgb']},
    }
}
