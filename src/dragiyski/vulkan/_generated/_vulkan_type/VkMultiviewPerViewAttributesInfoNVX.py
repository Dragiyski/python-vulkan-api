import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('perViewAttributes', ctypes.c_uint32),
        ('perViewAttributesPositionXOnly', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MULTIVIEW_PER_VIEW_ATTRIBUTES_INFO_NVX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'perViewAttributes': {'python_name': ['per', 'view', 'attributes']},
        'perViewAttributesPositionXOnly': {'python_name': ['per', 'view', 'attributes', 'position', 'xonly']},
    }
}
