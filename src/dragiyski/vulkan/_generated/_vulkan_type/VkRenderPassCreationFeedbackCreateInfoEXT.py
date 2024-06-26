import ctypes

class VkRenderPassCreationFeedbackCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderPassCreateInfo2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkRenderPassCreationFeedbackInfoEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pRenderPassFeedback': 'render_pass_feedback',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_subpass_merge_feedback',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_FEEDBACK_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_FEEDBACK_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRenderPassCreationFeedbackInfoEXT import VkRenderPassCreationFeedbackInfoEXT

VkRenderPassCreationFeedbackCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pRenderPassFeedback', ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT)),
]

VkRenderPassCreationFeedbackCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pRenderPassFeedback': ctypes.POINTER(VkRenderPassCreationFeedbackInfoEXT),
}
