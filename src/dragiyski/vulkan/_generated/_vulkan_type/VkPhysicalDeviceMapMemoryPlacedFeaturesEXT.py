import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryMapPlaced', ctypes.c_uint32),
        ('memoryMapRangePlaced', ctypes.c_uint32),
        ('memoryUnmapReserve', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAP_MEMORY_PLACED_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryMapPlaced': {'python_name': ['memory', 'map', 'placed']},
        'memoryMapRangePlaced': {'python_name': ['memory', 'map', 'range', 'placed']},
        'memoryUnmapReserve': {'python_name': ['memory', 'unmap', 'reserve']},
    }
}
