import ctypes

class VkPipelineColorBlendStateCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineColorBlendAdvancedStateCreateInfoEXT',
        'VkPipelineColorWriteCreateInfoEXT',
    }
    _includes_ = {
        'VkPipelineColorBlendAttachmentState',
    }
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'logicOpEnable': 'logic_op_enable',
        'logicOp': 'logic_op',
        'attachmentCount': 'attachment_count',
        'pAttachments': 'attachments',
        'blendConstants': 'blend_constants',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineColorBlendStateCreateFlags',
        'logicOp': 'VkLogicOp',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineColorBlendAttachmentState import VkPipelineColorBlendAttachmentState

VkPipelineColorBlendStateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('logicOpEnable', ctypes.c_uint32),
    ('logicOp', ctypes.c_int),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkPipelineColorBlendAttachmentState)),
    ('blendConstants', ctypes.ARRAY(ctypes.c_float, 4)),
]

VkPipelineColorBlendStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'logicOpEnable': ctypes.c_uint32,
    'logicOp': ctypes.c_int,
    'attachmentCount': ctypes.c_uint32,
    'pAttachments': ctypes.POINTER(VkPipelineColorBlendAttachmentState),
    'blendConstants': ctypes.ARRAY(ctypes.c_float, 4),
}
