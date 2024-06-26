import ctypes

class VkRenderPassCreateInfo2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkRenderPassCreationControlEXT',
        'VkRenderPassCreationFeedbackCreateInfoEXT',
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
    }
    _includes_ = {
        'VkAttachmentDescription2',
        'VkSubpassDependency2',
        'VkSubpassDescription2',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateRenderPass2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'attachmentCount': 'attachment_count',
        'pAttachments': 'attachments',
        'subpassCount': 'subpass_count',
        'pSubpasses': 'subpasses',
        'dependencyCount': 'dependency_count',
        'pDependencies': 'dependencies',
        'correlatedViewMaskCount': 'correlated_view_mask_count',
        'pCorrelatedViewMasks': 'correlated_view_masks',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkRenderPassCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAttachmentDescription2 import VkAttachmentDescription2
from .VkSubpassDependency2 import VkSubpassDependency2
from .VkSubpassDescription2 import VkSubpassDescription2

VkRenderPassCreateInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription2)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription2)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency2)),
    ('correlatedViewMaskCount', ctypes.c_uint32),
    ('pCorrelatedViewMasks', ctypes.POINTER(ctypes.c_uint32)),
]

VkRenderPassCreateInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'attachmentCount': ctypes.c_uint32,
    'pAttachments': ctypes.POINTER(VkAttachmentDescription2),
    'subpassCount': ctypes.c_uint32,
    'pSubpasses': ctypes.POINTER(VkSubpassDescription2),
    'dependencyCount': ctypes.c_uint32,
    'pDependencies': ctypes.POINTER(VkSubpassDependency2),
    'correlatedViewMaskCount': ctypes.c_uint32,
    'pCorrelatedViewMasks': ctypes.POINTER(ctypes.c_uint32),
}
