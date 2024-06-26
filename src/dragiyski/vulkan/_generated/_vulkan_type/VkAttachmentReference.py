import ctypes

class VkAttachmentReference(ctypes.Structure):
    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
        'VkSubpassDescription',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'attachment': 'attachment',
        'layout': 'layout',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'layout': 'VkImageLayout',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkAttachmentReference._type_ = {
    'attachment': ctypes.c_uint32,
    'layout': ctypes.c_int,
}
