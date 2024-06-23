import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoCodecOperations', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkQueueFamilyProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_VIDEO_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'videoCodecOperations': {'python_name': ['video', 'codec', 'operations'], 'type': 'VkVideoCodecOperationFlagsKHR'},
    }
}
