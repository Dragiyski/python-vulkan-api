import ctypes

class VkFramebufferAttachmentImageInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkFramebufferAttachmentsCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'usage': 'usage',
        'width': 'width',
        'height': 'height',
        'layerCount': 'layer_count',
        'viewFormatCount': 'view_format_count',
        'pViewFormats': 'view_formats',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkImageCreateFlags',
        'usage': 'VkImageUsageFlags',
        'pViewFormats': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAMEBUFFER_ATTACHMENT_IMAGE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkFramebufferAttachmentImageInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'usage': ctypes.c_uint32,
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'layerCount': ctypes.c_uint32,
    'viewFormatCount': ctypes.c_uint32,
    'pViewFormats': ctypes.POINTER(ctypes.c_int),
}
