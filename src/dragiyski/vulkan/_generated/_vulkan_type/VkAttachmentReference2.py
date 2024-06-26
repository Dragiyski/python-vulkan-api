import ctypes

class VkAttachmentReference2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
        ('aspectMask', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAttachmentReferenceStencilLayout',
    }
    _includes_ = set()
    _included_in_ = {
        'VkFragmentShadingRateAttachmentInfoKHR',
        'VkSubpassDescription2',
        'VkSubpassDescriptionDepthStencilResolve',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'attachment': 'attachment',
        'layout': 'layout',
        'aspectMask': 'aspect_mask',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'layout': 'VkImageLayout',
        'aspectMask': 'VkImageAspectFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkAttachmentReference2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachment': ctypes.c_uint32,
    'layout': ctypes.c_int,
    'aspectMask': ctypes.c_uint32,
}
