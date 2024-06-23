import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('windowExtent', VkExtent2D),
    ('windowCompareMode', ctypes.c_int),
]

descriptor = {
    'extends': {
        'VkSamplerCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_BLOCK_MATCH_WINDOW_CREATE_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'windowExtent': {'python_name': ['window', 'extent'], 'type': 'VkExtent2D'},
        'windowCompareMode': {'python_name': ['window', 'compare', 'mode'], 'type': 'VkBlockMatchWindowCompareModeQCOM'},
    }
}
