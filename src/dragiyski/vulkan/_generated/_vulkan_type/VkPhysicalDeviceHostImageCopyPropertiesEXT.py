import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('copySrcLayoutCount', ctypes.c_uint32),
        ('pCopySrcLayouts', ctypes.POINTER(ctypes.c_int)),
        ('copyDstLayoutCount', ctypes.c_uint32),
        ('pCopyDstLayouts', ctypes.POINTER(ctypes.c_int)),
        ('optimalTilingLayoutUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('identicalMemoryTypeRequirements', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_HOST_IMAGE_COPY_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'copySrcLayoutCount': {'python_name': ['copy', 'src', 'layout', 'count']},
        'pCopySrcLayouts': {'python_name': ['p', 'copy', 'src', 'layouts'], 'len': [['copySrcLayoutCount']], 'type': 'VkImageLayout'},
        'copyDstLayoutCount': {'python_name': ['copy', 'dst', 'layout', 'count']},
        'pCopyDstLayouts': {'python_name': ['p', 'copy', 'dst', 'layouts'], 'len': [['copyDstLayoutCount']], 'type': 'VkImageLayout'},
        'optimalTilingLayoutUUID': {'python_name': ['optimal', 'tiling', 'layout', 'uuid']},
        'identicalMemoryTypeRequirements': {'python_name': ['identical', 'memory', 'type', 'requirements']},
    }
}
