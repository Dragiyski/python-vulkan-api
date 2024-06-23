import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentDensityMap', ctypes.c_uint32),
        ('fragmentDensityMapDynamic', ctypes.c_uint32),
        ('fragmentDensityMapNonSubsampledImages', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_DENSITY_MAP_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentDensityMap': {'python_name': ['fragment', 'density', 'map']},
        'fragmentDensityMapDynamic': {'python_name': ['fragment', 'density', 'map', 'dynamic']},
        'fragmentDensityMapNonSubsampledImages': {'python_name': ['fragment', 'density', 'map', 'non', 'subsampled', 'images']},
    }
}
