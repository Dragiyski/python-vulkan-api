import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('address', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkDescriptorBufferBindingPushDescriptorBufferHandleEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdBindDescriptorBuffersEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_BUFFER_BINDING_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'address': {'python_name': ['address']},
        'usage': {'python_name': ['usage'], 'type': 'VkBufferUsageFlags'},
    }
}
