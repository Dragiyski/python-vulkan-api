import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('maxExtent', VkExtent3D),
    ('maxMipLevels', ctypes.c_uint32),
    ('maxArrayLayers', ctypes.c_uint32),
    ('sampleCounts', ctypes.c_uint32),
    ('maxResourceSize', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
    },
    'included_in': {
        'VkExternalImageFormatPropertiesNV',
        'VkImageFormatProperties2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceImageFormatProperties',
    },
    'member_map': {
        'maxExtent': {'python_name': ['max', 'extent'], 'type': 'VkExtent3D'},
        'maxMipLevels': {'python_name': ['max', 'mip', 'levels']},
        'maxArrayLayers': {'python_name': ['max', 'array', 'layers']},
        'sampleCounts': {'python_name': ['sample', 'counts'], 'type': 'VkSampleCountFlags'},
        'maxResourceSize': {'python_name': ['max', 'resource', 'size']},
    }
}
