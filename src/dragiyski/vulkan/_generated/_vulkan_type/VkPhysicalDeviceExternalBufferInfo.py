import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBufferUsageFlags2CreateInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceExternalBufferProperties',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_BUFFER_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkBufferCreateFlags'},
        'usage': {'python_name': ['usage'], 'type': 'VkBufferUsageFlags'},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalMemoryHandleTypeFlagBits'},
    }
}
