import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryResultStatusSupport', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_QUERY_RESULT_STATUS_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'queryResultStatusSupport': {'python_name': ['query', 'result', 'status', 'support']},
    }
}
