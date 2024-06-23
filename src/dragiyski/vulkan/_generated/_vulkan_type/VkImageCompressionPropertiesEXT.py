import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageCompressionFlags', ctypes.c_uint32),
        ('imageCompressionFixedRateFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkImageFormatProperties2',
        'VkSubresourceLayout2KHR',
        'VkSurfaceFormat2KHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageCompressionFlags': {'python_name': ['image', 'compression', 'flags'], 'type': 'VkImageCompressionFlagsEXT'},
        'imageCompressionFixedRateFlags': {'python_name': ['image', 'compression', 'fixed', 'rate', 'flags'], 'type': 'VkImageCompressionFixedRateFlagsEXT'},
    }
}
