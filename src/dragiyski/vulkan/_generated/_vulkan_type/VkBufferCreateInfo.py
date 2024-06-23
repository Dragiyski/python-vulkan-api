import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('size', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBufferCollectionBufferCreateInfoFUCHSIA',
        'VkBufferDeviceAddressCreateInfoEXT',
        'VkBufferOpaqueCaptureAddressCreateInfo',
        'VkBufferUsageFlags2CreateInfoKHR',
        'VkDedicatedAllocationBufferCreateInfoNV',
        'VkExternalMemoryBufferCreateInfo',
        'VkOpaqueCaptureDescriptorDataCreateInfoEXT',
        'VkVideoProfileListInfoKHR',
    },
    'includes': set(),
    'included_in': {
        'VkBufferConstraintsInfoFUCHSIA',
        'VkDeviceBufferMemoryRequirements',
    },
    'input_of': {
        'vkCreateBuffer',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkBufferCreateFlags'},
        'size': {'python_name': ['size']},
        'usage': {'python_name': ['usage'], 'type': 'VkBufferUsageFlags'},
        'sharingMode': {'python_name': ['sharing', 'mode'], 'type': 'VkSharingMode'},
        'queueFamilyIndexCount': {'python_name': ['queue', 'family', 'index', 'count']},
        'pQueueFamilyIndices': {'python_name': ['p', 'queue', 'family', 'indices'], 'len': [['queueFamilyIndexCount']]},
    }
}
