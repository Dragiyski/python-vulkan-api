import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdPipelineBarrier',
        'vkCmdWaitEvents',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_BARRIER', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags'},
    }
}
