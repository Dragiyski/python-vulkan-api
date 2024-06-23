import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkExportFenceCreateInfo',
        'VkExportFenceSciSyncInfoNV',
        'VkExportFenceWin32HandleInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateFence',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FENCE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkFenceCreateFlags'},
    }
}
