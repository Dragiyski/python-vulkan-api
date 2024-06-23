import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('extendedSparseAddressSpaceSize', ctypes.c_uint64),
        ('extendedSparseImageUsageFlags', ctypes.c_uint32),
        ('extendedSparseBufferUsageFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTENDED_SPARSE_ADDRESS_SPACE_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'extendedSparseAddressSpaceSize': {'python_name': ['extended', 'sparse', 'address', 'space', 'size']},
        'extendedSparseImageUsageFlags': {'python_name': ['extended', 'sparse', 'image', 'usage', 'flags'], 'type': 'VkImageUsageFlags'},
        'extendedSparseBufferUsageFlags': {'python_name': ['extended', 'sparse', 'buffer', 'usage', 'flags'], 'type': 'VkBufferUsageFlags'},
    }
}
