import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('type', ctypes.c_int),
        ('memoryObjectId', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('heapIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_REPORT_CALLBACK_DATA_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDeviceMemoryReportFlagsEXT'},
        'type': {'python_name': ['type'], 'type': 'VkDeviceMemoryReportEventTypeEXT'},
        'memoryObjectId': {'python_name': ['memory', 'object', 'id']},
        'size': {'python_name': ['size']},
        'objectType': {'python_name': ['object', 'type'], 'type': 'VkObjectType'},
        'objectHandle': {'python_name': ['object', 'handle']},
        'heapIndex': {'python_name': ['heap', 'index']},
    }
}
