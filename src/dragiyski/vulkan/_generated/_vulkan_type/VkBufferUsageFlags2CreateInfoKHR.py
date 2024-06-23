import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkBufferCreateInfo',
        'VkBufferViewCreateInfo',
        'VkDescriptorBufferBindingInfoEXT',
        'VkPhysicalDeviceExternalBufferInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_USAGE_FLAGS_2_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'usage': {'python_name': ['usage'], 'type': 'VkBufferUsageFlags2KHR'},
    }
}
