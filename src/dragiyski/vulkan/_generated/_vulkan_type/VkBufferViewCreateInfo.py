import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkExportMetalObjectCreateInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateBufferView',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_VIEW_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkBufferViewCreateFlags'},
        'buffer': {'python_name': ['buffer']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'offset': {'python_name': ['offset']},
        'range': {'python_name': ['range']},
    }
}
