import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('compressionControlPlaneCount', ctypes.c_uint32),
        ('pFixedRateFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
        'VkSwapchainCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkImageCompressionFlagsEXT'},
        'compressionControlPlaneCount': {'python_name': ['compression', 'control', 'plane', 'count']},
        'pFixedRateFlags': {'python_name': ['p', 'fixed', 'rate', 'flags'], 'len': [['compressionControlPlaneCount']], 'type': 'VkImageCompressionFixedRateFlagsEXT'},
    }
}
