import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkCommandBufferBeginInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_COMMAND_BUFFER_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceMask': {'python_name': ['device', 'mask']},
    }
}
