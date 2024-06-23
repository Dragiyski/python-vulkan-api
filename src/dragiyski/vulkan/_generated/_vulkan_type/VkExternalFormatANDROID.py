import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('externalFormat', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkAttachmentDescription2',
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
        'VkImageCreateInfo',
        'VkSamplerYcbcrConversionCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_ANDROID', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'externalFormat': {'python_name': ['external', 'format']},
    }
}
