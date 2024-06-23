import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priorityCount', ctypes.c_uint32),
        ('priorities', ctypes.ARRAY(ctypes.c_int, 16)),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_GLOBAL_PRIORITY_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'priorityCount': {'python_name': ['priority', 'count']},
        'priorities': {'python_name': ['priorities'], 'len': [['priorityCount']], 'type': 'VkQueueGlobalPriorityKHR'},
    }
}
