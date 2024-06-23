import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateTexelSize', VkExtent2D),
    ('shadingRatePaletteSize', ctypes.c_uint32),
    ('shadingRateMaxCoarseSamples', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shadingRateTexelSize': {'python_name': ['shading', 'rate', 'texel', 'size'], 'type': 'VkExtent2D'},
        'shadingRatePaletteSize': {'python_name': ['shading', 'rate', 'palette', 'size']},
        'shadingRateMaxCoarseSamples': {'python_name': ['shading', 'rate', 'max', 'coarse', 'samples']},
    }
}
