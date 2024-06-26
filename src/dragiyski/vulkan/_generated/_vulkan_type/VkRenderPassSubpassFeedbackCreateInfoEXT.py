import ctypes

class VkRenderPassSubpassFeedbackCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkSubpassDescription2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRenderPassSubpassFeedbackInfoEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pSubpassFeedback': 'subpass_feedback',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_subpass_merge_feedback',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_SUBPASS_FEEDBACK_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_SUBPASS_FEEDBACK_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRenderPassSubpassFeedbackInfoEXT import VkRenderPassSubpassFeedbackInfoEXT

VkRenderPassSubpassFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pSubpassFeedback', ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT)),
]

VkRenderPassSubpassFeedbackCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pSubpassFeedback': ctypes.POINTER(VkRenderPassSubpassFeedbackInfoEXT),
}
