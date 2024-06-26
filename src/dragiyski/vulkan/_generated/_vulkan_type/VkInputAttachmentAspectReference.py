import ctypes

class VkInputAttachmentAspectReference(ctypes.Structure):
    _fields_ = [
        ('subpass', ctypes.c_uint32),
        ('inputAttachmentIndex', ctypes.c_uint32),
        ('aspectMask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassInputAttachmentAspectCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'subpass': 'subpass',
        'inputAttachmentIndex': 'input_attachment_index',
        'aspectMask': 'aspect_mask',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'aspectMask': 'VkImageAspectFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkInputAttachmentAspectReference._type_ = {
    'subpass': ctypes.c_uint32,
    'inputAttachmentIndex': ctypes.c_uint32,
    'aspectMask': ctypes.c_uint32,
}
