import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorUpdateTemplate', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdPushDescriptorSetWithTemplate2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_WITH_TEMPLATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorUpdateTemplate': {'python_name': ['descriptor', 'update', 'template']},
        'layout': {'python_name': ['layout']},
        'set': {'python_name': ['set']},
        'pData': {'python_name': ['p', 'data']},
    }
}
