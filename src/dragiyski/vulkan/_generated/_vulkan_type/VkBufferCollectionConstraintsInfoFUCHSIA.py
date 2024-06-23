import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minBufferCount', ctypes.c_uint32),
        ('maxBufferCount', ctypes.c_uint32),
        ('minBufferCountForCamping', ctypes.c_uint32),
        ('minBufferCountForDedicatedSlack', ctypes.c_uint32),
        ('minBufferCountForSharedSlack', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkBufferConstraintsInfoFUCHSIA',
        'VkImageConstraintsInfoFUCHSIA',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_CONSTRAINTS_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'minBufferCount': {'python_name': ['min', 'buffer', 'count']},
        'maxBufferCount': {'python_name': ['max', 'buffer', 'count']},
        'minBufferCountForCamping': {'python_name': ['min', 'buffer', 'count', 'for', 'camping']},
        'minBufferCountForDedicatedSlack': {'python_name': ['min', 'buffer', 'count', 'for', 'dedicated', 'slack']},
        'minBufferCountForSharedSlack': {'python_name': ['min', 'buffer', 'count', 'for', 'shared', 'slack']},
    }
}
