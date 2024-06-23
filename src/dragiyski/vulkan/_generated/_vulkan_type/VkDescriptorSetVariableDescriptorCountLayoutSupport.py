import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxVariableDescriptorCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDescriptorSetLayoutSupport',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_LAYOUT_SUPPORT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxVariableDescriptorCount': {'python_name': ['max', 'variable', 'descriptor', 'count']},
    }
}
