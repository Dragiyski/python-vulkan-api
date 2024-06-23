import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentLocations', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetRenderingAttachmentLocationsKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_LOCATION_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachmentLocations': {'python_name': ['p', 'color', 'attachment', 'locations'], 'len': [['colorAttachmentCount']]},
    }
}
