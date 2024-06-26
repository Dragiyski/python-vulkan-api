import ctypes

class VkFramebufferCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('renderPass', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layers', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkFramebufferAttachmentsCreateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateFramebuffer',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'renderPass': 'render_pass',
        'attachmentCount': 'attachment_count',
        'pAttachments': 'attachments',
        'width': 'width',
        'height': 'height',
        'layers': 'layers',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkFramebufferCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkFramebufferCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'renderPass': ctypes.c_void_p,
    'attachmentCount': ctypes.c_uint32,
    'pAttachments': ctypes.POINTER(ctypes.c_void_p),
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'layers': ctypes.c_uint32,
}
