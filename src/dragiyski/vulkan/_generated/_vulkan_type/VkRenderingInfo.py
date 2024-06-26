import ctypes

class VkRenderingInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceGroupRenderPassBeginInfo',
        'VkMultisampledRenderToSingleSampledInfoEXT',
        'VkMultiviewPerViewAttributesInfoNVX',
        'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM',
        'VkRenderPassStripeBeginInfoARM',
        'VkRenderingFragmentDensityMapAttachmentInfoEXT',
        'VkRenderingFragmentShadingRateAttachmentInfoKHR',
    }
    _includes_ = {
        'VkRect2D',
        'VkRenderingAttachmentInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBeginRendering',
        'vkGetDynamicRenderingTilePropertiesQCOM',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'renderArea': 'render_area',
        'layerCount': 'layer_count',
        'viewMask': 'view_mask',
        'colorAttachmentCount': 'color_attachment_count',
        'pColorAttachments': 'color_attachments',
        'pDepthAttachment': 'depth_attachment',
        'pStencilAttachment': 'stencil_attachment',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkRenderingFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDERING_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkRect2D import VkRect2D
from .VkRenderingAttachmentInfo import VkRenderingAttachmentInfo

VkRenderingInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('renderArea', VkRect2D),
    ('layerCount', ctypes.c_uint32),
    ('viewMask', ctypes.c_uint32),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pDepthAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pStencilAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
]

VkRenderingInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'renderArea': VkRect2D,
    'layerCount': ctypes.c_uint32,
    'viewMask': ctypes.c_uint32,
    'colorAttachmentCount': ctypes.c_uint32,
    'pColorAttachments': ctypes.POINTER(VkRenderingAttachmentInfo),
    'pDepthAttachment': ctypes.POINTER(VkRenderingAttachmentInfo),
    'pStencilAttachment': ctypes.POINTER(VkRenderingAttachmentInfo),
}
