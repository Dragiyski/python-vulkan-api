import ctypes

class VkRenderPassSubpassFeedbackInfoEXT(ctypes.Structure):
    _fields_ = [
        ('subpassMergeStatus', ctypes.c_int),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('postMergeIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassSubpassFeedbackCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'subpassMergeStatus': 'subpass_merge_status',
        'description': 'description',
        'postMergeIndex': 'post_merge_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_subpass_merge_feedback',
    }
    _vk_enum_ = {
        'subpassMergeStatus': 'VkSubpassMergeStatusEXT',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkRenderPassSubpassFeedbackInfoEXT._type_ = {
    'subpassMergeStatus': ctypes.c_int,
    'description': ctypes.ARRAY(ctypes.c_char, 256),
    'postMergeIndex': ctypes.c_uint32,
}
