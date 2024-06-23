import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('overallocationBehavior', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'overallocationBehavior': {'python_name': ['overallocation', 'behavior'], 'type': 'VkMemoryOverallocationBehaviorAMD'},
    }
}
