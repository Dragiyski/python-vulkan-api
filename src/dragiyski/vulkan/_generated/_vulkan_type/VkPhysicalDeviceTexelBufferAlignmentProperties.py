import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('storageTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
        ('uniformTexelBufferOffsetAlignmentBytes', ctypes.c_uint64),
        ('uniformTexelBufferOffsetSingleTexelAlignment', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_TEXEL_BUFFER_ALIGNMENT_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'storageTexelBufferOffsetAlignmentBytes': {'python_name': ['storage', 'texel', 'buffer', 'offset', 'alignment', 'bytes']},
        'storageTexelBufferOffsetSingleTexelAlignment': {'python_name': ['storage', 'texel', 'buffer', 'offset', 'single', 'texel', 'alignment']},
        'uniformTexelBufferOffsetAlignmentBytes': {'python_name': ['uniform', 'texel', 'buffer', 'offset', 'alignment', 'bytes']},
        'uniformTexelBufferOffsetSingleTexelAlignment': {'python_name': ['uniform', 'texel', 'buffer', 'offset', 'single', 'texel', 'alignment']},
    }
}
