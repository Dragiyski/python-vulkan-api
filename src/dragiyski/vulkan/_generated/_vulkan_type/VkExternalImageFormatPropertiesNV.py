import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageFormatProperties import CType as VkImageFormatProperties

CType._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageFormatProperties',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceExternalImageFormatPropertiesNV',
    },
    'member_map': {
        'imageFormatProperties': {'python_name': ['image', 'format', 'properties'], 'type': 'VkImageFormatProperties'},
        'externalMemoryFeatures': {'python_name': ['external', 'memory', 'features'], 'type': 'VkExternalMemoryFeatureFlagsNV'},
        'exportFromImportedHandleTypes': {'python_name': ['export', 'from', 'imported', 'handle', 'types'], 'type': 'VkExternalMemoryHandleTypeFlagsNV'},
        'compatibleHandleTypes': {'python_name': ['compatible', 'handle', 'types'], 'type': 'VkExternalMemoryHandleTypeFlagsNV'},
    }
}
