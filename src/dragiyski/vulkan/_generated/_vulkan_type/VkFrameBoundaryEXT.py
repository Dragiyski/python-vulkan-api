import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('frameID', ctypes.c_uint64),
        ('imageCount', ctypes.c_uint32),
        ('pImages', ctypes.POINTER(ctypes.c_void_p)),
        ('bufferCount', ctypes.c_uint32),
        ('pBuffers', ctypes.POINTER(ctypes.c_void_p)),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkBindSparseInfo',
        'VkPresentInfoKHR',
        'VkSubmitInfo',
        'VkSubmitInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAME_BOUNDARY_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkFrameBoundaryFlagsEXT'},
        'frameID': {'python_name': ['frame', 'id']},
        'imageCount': {'python_name': ['image', 'count']},
        'pImages': {'python_name': ['p', 'images'], 'len': [['imageCount']]},
        'bufferCount': {'python_name': ['buffer', 'count']},
        'pBuffers': {'python_name': ['p', 'buffers'], 'len': [['bufferCount']]},
        'tagName': {'python_name': ['tag', 'name']},
        'tagSize': {'python_name': ['tag', 'size']},
        'pTag': {'python_name': ['p', 'tag'], 'len': [['tagSize']]},
    }
}
