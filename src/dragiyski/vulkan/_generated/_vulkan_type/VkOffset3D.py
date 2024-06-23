import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('z', ctypes.c_int32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkBufferImageCopy',
        'VkBufferImageCopy2',
        'VkCopyMemoryToImageIndirectCommandNV',
        'VkImageBlit',
        'VkImageBlit2',
        'VkImageCopy',
        'VkImageCopy2',
        'VkImageResolve',
        'VkImageResolve2',
        'VkImageToMemoryCopyEXT',
        'VkMemoryToImageCopyEXT',
        'VkSparseImageMemoryBind',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x']},
        'y': {'python_name': ['y']},
        'z': {'python_name': ['z']},
    }
}
