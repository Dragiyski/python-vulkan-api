import ctypes

class CType(ctypes.Structure):
    pass

from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetCount', ctypes.c_uint32),
    ('pFragmentDensityOffsets', ctypes.POINTER(VkOffset2D)),
]

descriptor = {
    'extends': {
        'VkSubpassEndInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkOffset2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_FRAGMENT_DENSITY_MAP_OFFSET_END_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentDensityOffsetCount': {'python_name': ['fragment', 'density', 'offset', 'count']},
        'pFragmentDensityOffsets': {'python_name': ['p', 'fragment', 'density', 'offsets'], 'len': [['fragmentDensityOffsetCount']], 'type': 'VkOffset2D'},
    }
}
