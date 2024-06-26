import ctypes

class VkAttachmentDescription(ctypes.Structure):
    _fields_ = [
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
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkRenderPassCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
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
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'flags': 'VkAttachmentDescriptionFlags',
        'format': 'VkFormat',
        'loadOp': 'VkAttachmentLoadOp',
        'storeOp': 'VkAttachmentStoreOp',
        'stencilLoadOp': 'VkAttachmentLoadOp',
        'stencilStoreOp': 'VkAttachmentStoreOp',
        'initialLayout': 'VkImageLayout',
        'finalLayout': 'VkImageLayout',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkAttachmentDescription._type_ = {
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
