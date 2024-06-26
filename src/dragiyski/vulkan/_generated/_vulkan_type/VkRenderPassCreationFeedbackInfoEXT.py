import ctypes

class VkRenderPassCreationFeedbackInfoEXT(ctypes.Structure):
    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassCreationFeedbackCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'postMergeSubpassCount': 'post_merge_subpass_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_subpass_merge_feedback',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkRenderPassCreationFeedbackInfoEXT._type_ = {
    'postMergeSubpassCount': ctypes.c_uint32,
}
