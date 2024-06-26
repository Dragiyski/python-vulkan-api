import ctypes

class VkFragmentShadingRateAttachmentInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkSubpassDescription2',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkAttachmentReference2',
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pFragmentShadingRateAttachment': 'fragment_shading_rate_attachment',
        'shadingRateAttachmentTexelSize': 'shading_rate_attachment_texel_size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_fragment_shading_rate',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAttachmentReference2 import VkAttachmentReference2
from .VkExtent2D import VkExtent2D

VkFragmentShadingRateAttachmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

VkFragmentShadingRateAttachmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pFragmentShadingRateAttachment': ctypes.POINTER(VkAttachmentReference2),
    'shadingRateAttachmentTexelSize': VkExtent2D,
}
