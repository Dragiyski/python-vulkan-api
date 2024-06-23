import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorOffset', ctypes.c_size_t),
        ('descriptorSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_HOST_MAPPING_INFO_VALVE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorOffset': {'python_name': ['descriptor', 'offset']},
        'descriptorSize': {'python_name': ['descriptor', 'size']},
    }
}
