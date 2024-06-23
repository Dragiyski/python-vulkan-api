import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkExtent3D import CType as VkExtent3D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('tileSize', VkExtent3D),
    ('apronSize', VkExtent2D),
    ('origin', VkOffset2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkExtent3D',
        'VkOffset2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDynamicRenderingTilePropertiesQCOM',
        'vkGetFramebufferTilePropertiesQCOM',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_TILE_PROPERTIES_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'tileSize': {'python_name': ['tile', 'size'], 'type': 'VkExtent3D'},
        'apronSize': {'python_name': ['apron', 'size'], 'type': 'VkExtent2D'},
        'origin': {'python_name': ['origin'], 'type': 'VkOffset2D'},
    }
}
