import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('srcQueueFamilyIndex', ctypes.c_uint32),
        ('dstQueueFamilyIndex', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExternalMemoryAcquireUnmodifiedEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdPipelineBarrier',
        'vkCmdWaitEvents',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_MEMORY_BARRIER', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'srcQueueFamilyIndex': {'python_name': ['src', 'queue', 'family', 'index']},
        'dstQueueFamilyIndex': {'python_name': ['dst', 'queue', 'family', 'index']},
        'buffer': {'python_name': ['buffer']},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
    }
}
