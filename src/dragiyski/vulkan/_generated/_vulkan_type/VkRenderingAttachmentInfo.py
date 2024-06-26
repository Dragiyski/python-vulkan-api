import ctypes

class VkRenderingAttachmentInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkClearValue',
    }
    _included_in_ = {
        'VkRenderingInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageView': 'image_view',
        'imageLayout': 'image_layout',
        'resolveMode': 'resolve_mode',
        'resolveImageView': 'resolve_image_view',
        'resolveImageLayout': 'resolve_image_layout',
        'loadOp': 'load_op',
        'storeOp': 'store_op',
        'clearValue': 'clear_value',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'imageLayout': 'VkImageLayout',
        'resolveImageLayout': 'VkImageLayout',
        'loadOp': 'VkAttachmentLoadOp',
        'storeOp': 'VkAttachmentStoreOp',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkClearValue import VkClearValue

VkRenderingAttachmentInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('resolveMode', ctypes.c_uint32),
    ('resolveImageView', ctypes.c_void_p),
    ('resolveImageLayout', ctypes.c_int),
    ('loadOp', ctypes.c_int),
    ('storeOp', ctypes.c_int),
    ('clearValue', VkClearValue),
]

VkRenderingAttachmentInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
    'resolveMode': ctypes.c_uint32,
    'resolveImageView': ctypes.c_void_p,
    'resolveImageLayout': ctypes.c_int,
    'loadOp': ctypes.c_int,
    'storeOp': ctypes.c_int,
    'clearValue': VkClearValue,
}
