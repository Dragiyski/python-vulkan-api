import ctypes

class VkAttachmentDescription2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('loadOp', ctypes.c_int),
        ('storeOp', ctypes.c_int),
        ('stencilLoadOp', ctypes.c_int),
        ('stencilStoreOp', ctypes.c_int),
        ('initialLayout', ctypes.c_int),
        ('finalLayout', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAttachmentDescriptionStencilLayout',
        'VkExternalFormatANDROID',
    }
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassCreateInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'format': 'format',
        'samples': 'samples',
        'loadOp': 'load_op',
        'storeOp': 'store_op',
        'stencilLoadOp': 'stencil_load_op',
        'stencilStoreOp': 'stencil_store_op',
        'initialLayout': 'initial_layout',
        'finalLayout': 'final_layout',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkAttachmentDescriptionFlags',
        'format': 'VkFormat',
        'loadOp': 'VkAttachmentLoadOp',
        'storeOp': 'VkAttachmentStoreOp',
        'stencilLoadOp': 'VkAttachmentLoadOp',
        'stencilStoreOp': 'VkAttachmentStoreOp',
        'initialLayout': 'VkImageLayout',
        'finalLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_2
        for function in self._init_:
            function(self, *args, **kwargs)

VkAttachmentDescription2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'format': ctypes.c_int,
    'samples': ctypes.c_uint32,
    'loadOp': ctypes.c_int,
    'storeOp': ctypes.c_int,
    'stencilLoadOp': ctypes.c_int,
    'stencilStoreOp': ctypes.c_int,
    'initialLayout': ctypes.c_int,
    'finalLayout': ctypes.c_int,
}
