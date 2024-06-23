import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo
from .VkSysmemColorSpaceFUCHSIA import CType as VkSysmemColorSpaceFUCHSIA

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageCreateInfo', VkImageCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('colorSpaceCount', ctypes.c_uint32),
    ('pColorSpaces', ctypes.POINTER(VkSysmemColorSpaceFUCHSIA)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageCreateInfo',
        'VkSysmemColorSpaceFUCHSIA',
    },
    'included_in': {
        'VkImageConstraintsInfoFUCHSIA',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_CONSTRAINTS_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageCreateInfo': {'python_name': ['image', 'create', 'info'], 'type': 'VkImageCreateInfo'},
        'requiredFormatFeatures': {'python_name': ['required', 'format', 'features'], 'type': 'VkFormatFeatureFlags'},
        'flags': {'python_name': ['flags'], 'type': 'VkImageFormatConstraintsFlagsFUCHSIA'},
        'sysmemPixelFormat': {'python_name': ['sysmem', 'pixel', 'format']},
        'colorSpaceCount': {'python_name': ['color', 'space', 'count']},
        'pColorSpaces': {'python_name': ['p', 'color', 'spaces'], 'len': [['colorSpaceCount']], 'type': 'VkSysmemColorSpaceFUCHSIA'},
    }
}
