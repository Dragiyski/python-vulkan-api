import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPass', ctypes.c_void_p),
        ('subpass', ctypes.c_uint32),
        ('framebuffer', ctypes.c_void_p),
        ('occlusionQueryEnable', ctypes.c_uint32),
        ('queryFlags', ctypes.c_uint32),
        ('pipelineStatistics', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAttachmentSampleCountInfoAMD',
        'VkCommandBufferInheritanceConditionalRenderingInfoEXT',
        'VkCommandBufferInheritanceRenderPassTransformInfoQCOM',
        'VkCommandBufferInheritanceRenderingInfo',
        'VkCommandBufferInheritanceViewportScissorInfoNV',
        'VkExternalFormatANDROID',
        'VkMultiviewPerViewAttributesInfoNVX',
        'VkRenderingAttachmentLocationInfoKHR',
        'VkRenderingInputAttachmentIndexInfoKHR',
    },
    'includes': set(),
    'included_in': {
        'VkCommandBufferBeginInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'renderPass': {'python_name': ['render', 'pass']},
        'subpass': {'python_name': ['subpass']},
        'framebuffer': {'python_name': ['framebuffer']},
        'occlusionQueryEnable': {'python_name': ['occlusion', 'query', 'enable']},
        'queryFlags': {'python_name': ['query', 'flags'], 'type': 'VkQueryControlFlags'},
        'pipelineStatistics': {'python_name': ['pipeline', 'statistics'], 'type': 'VkQueryPipelineStatisticFlags'},
    }
}
