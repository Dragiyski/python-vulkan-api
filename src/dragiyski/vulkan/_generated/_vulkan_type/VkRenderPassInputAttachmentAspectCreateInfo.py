import ctypes

class VkRenderPassInputAttachmentAspectCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderPassCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkInputAttachmentAspectReference',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'aspectReferenceCount': 'aspect_reference_count',
        'pAspectReferences': 'aspect_references',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_INPUT_ATTACHMENT_ASPECT_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkInputAttachmentAspectReference import VkInputAttachmentAspectReference

VkRenderPassInputAttachmentAspectCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('aspectReferenceCount', ctypes.c_uint32),
    ('pAspectReferences', ctypes.POINTER(VkInputAttachmentAspectReference)),
]

VkRenderPassInputAttachmentAspectCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'aspectReferenceCount': ctypes.c_uint32,
    'pAspectReferences': ctypes.POINTER(VkInputAttachmentAspectReference),
}
