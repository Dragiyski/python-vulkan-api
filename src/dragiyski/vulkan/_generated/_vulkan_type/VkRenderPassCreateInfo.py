import ctypes

class VkRenderPassCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
        'VkRenderPassInputAttachmentAspectCreateInfo',
        'VkRenderPassMultiviewCreateInfo',
    }
    _includes_ = {
        'VkAttachmentDescription',
        'VkSubpassDependency',
        'VkSubpassDescription',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateRenderPass',
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
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkRenderPassCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAttachmentDescription import VkAttachmentDescription
from .VkSubpassDependency import VkSubpassDependency
from .VkSubpassDescription import VkSubpassDescription

VkRenderPassCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkAttachmentDescription)),
    ('subpassCount', ctypes.c_uint32),
    ('pSubpasses', ctypes.POINTER(VkSubpassDescription)),
    ('dependencyCount', ctypes.c_uint32),
    ('pDependencies', ctypes.POINTER(VkSubpassDependency)),
]

VkRenderPassCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'attachmentCount': ctypes.c_uint32,
    'pAttachments': ctypes.POINTER(VkAttachmentDescription),
    'subpassCount': ctypes.c_uint32,
    'pSubpasses': ctypes.POINTER(VkSubpassDescription),
    'dependencyCount': ctypes.c_uint32,
    'pDependencies': ctypes.POINTER(VkSubpassDependency),
}
