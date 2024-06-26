import ctypes

class VkClearAttachment(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkClearValue',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdClearAttachments',
    }
    _output_of_ = set()
    _python_name_ = {
        'aspectMask': 'aspect_mask',
        'colorAttachment': 'color_attachment',
        'clearValue': 'clear_value',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'aspectMask': 'VkImageAspectFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkClearValue import VkClearValue

VkClearAttachment._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]

VkClearAttachment._type_ = {
    'aspectMask': ctypes.c_uint32,
    'colorAttachment': ctypes.c_uint32,
    'clearValue': VkClearValue,
}
