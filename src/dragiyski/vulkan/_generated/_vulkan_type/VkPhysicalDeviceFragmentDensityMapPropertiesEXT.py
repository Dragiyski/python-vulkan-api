import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentDensityTexelSize', VkExtent2D),
    ('maxFragmentDensityTexelSize', VkExtent2D),
    ('fragmentDensityInvocations', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'minFragmentDensityTexelSize': {'python_name': ['min', 'fragment', 'density', 'texel', 'size'], 'type': 'VkExtent2D'},
        'maxFragmentDensityTexelSize': {'python_name': ['max', 'fragment', 'density', 'texel', 'size'], 'type': 'VkExtent2D'},
        'fragmentDensityInvocations': {'python_name': ['fragment', 'density', 'invocations']},
    }
}
