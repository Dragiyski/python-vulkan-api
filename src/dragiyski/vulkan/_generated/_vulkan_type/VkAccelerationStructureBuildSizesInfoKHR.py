import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructureSize', ctypes.c_uint64),
        ('updateScratchSize', ctypes.c_uint64),
        ('buildScratchSize', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetAccelerationStructureBuildSizesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_BUILD_SIZES_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'accelerationStructureSize': {'python_name': ['acceleration', 'structure', 'size']},
        'updateScratchSize': {'python_name': ['update', 'scratch', 'size']},
        'buildScratchSize': {'python_name': ['build', 'scratch', 'size']},
    }
}
