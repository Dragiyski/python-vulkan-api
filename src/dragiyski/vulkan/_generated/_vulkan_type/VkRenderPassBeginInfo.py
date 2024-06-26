import ctypes

class VkRenderPassBeginInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceGroupRenderPassBeginInfo',
        'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM',
        'VkRenderPassAttachmentBeginInfo',
        'VkRenderPassSampleLocationsBeginInfoEXT',
        'VkRenderPassStripeBeginInfoARM',
        'VkRenderPassTransformBeginInfoQCOM',
    }
    _includes_ = {
        'VkClearValue',
        'VkRect2D',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBeginRenderPass',
        'vkCmdBeginRenderPass2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'renderPass': 'render_pass',
        'framebuffer': 'framebuffer',
        'renderArea': 'render_area',
        'clearValueCount': 'clear_value_count',
        'pClearValues': 'clear_values',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkClearValue import VkClearValue
from .VkRect2D import VkRect2D

VkRenderPassBeginInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('framebuffer', ctypes.c_void_p),
    ('renderArea', VkRect2D),
    ('clearValueCount', ctypes.c_uint32),
    ('pClearValues', ctypes.POINTER(VkClearValue)),
]

VkRenderPassBeginInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPass': ctypes.c_void_p,
    'framebuffer': ctypes.c_void_p,
    'renderArea': VkRect2D,
    'clearValueCount': ctypes.c_uint32,
    'pClearValues': ctypes.POINTER(VkClearValue),
}
