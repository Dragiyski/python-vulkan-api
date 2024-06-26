import ctypes

class VkRenderingFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkRenderingInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'imageView': 'image_view',
        'imageLayout': 'image_layout',
        'shadingRateAttachmentTexelSize': 'shading_rate_attachment_texel_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_dynamic_rendering',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'imageLayout': 'VkImageLayout',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkRenderingFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

VkRenderingFragmentShadingRateAttachmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageView': ctypes.c_void_p,
    'imageLayout': ctypes.c_int,
    'shadingRateAttachmentTexelSize': VkExtent2D,
}
