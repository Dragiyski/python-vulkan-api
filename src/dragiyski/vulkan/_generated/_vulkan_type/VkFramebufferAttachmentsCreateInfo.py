import ctypes

class VkFramebufferAttachmentsCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkFramebufferCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkFramebufferAttachmentImageInfo',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'attachmentImageInfoCount': 'attachment_image_info_count',
        'pAttachmentImageInfos': 'attachment_image_infos',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENTS_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkFramebufferAttachmentImageInfo import VkFramebufferAttachmentImageInfo

VkFramebufferAttachmentsCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('attachmentImageInfoCount', ctypes.c_uint32),
    ('pAttachmentImageInfos', ctypes.POINTER(VkFramebufferAttachmentImageInfo)),
]

VkFramebufferAttachmentsCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'attachmentImageInfoCount': ctypes.c_uint32,
    'pAttachmentImageInfos': ctypes.POINTER(VkFramebufferAttachmentImageInfo),
}
