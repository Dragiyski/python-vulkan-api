import ctypes

class VkRect2D(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
        'VkOffset2D',
    }
    _included_in_ = {
        'VkBindImageMemoryDeviceGroupInfo',
        'VkClearRect',
        'VkCommandBufferInheritanceRenderPassTransformInfoQCOM',
        'VkDeviceGroupRenderPassBeginInfo',
        'VkDisplayPresentInfoKHR',
        'VkMultiviewPerViewRenderAreasRenderPassBeginInfoQCOM',
        'VkOpticalFlowExecuteInfoNV',
        'VkPipelineDiscardRectangleStateCreateInfoEXT',
        'VkPipelineViewportExclusiveScissorStateCreateInfoNV',
        'VkPipelineViewportStateCreateInfo',
        'VkRenderPassBeginInfo',
        'VkRenderPassStripeInfoARM',
        'VkRenderingInfo',
    }
    _input_of_ = {
        'vkCmdSetDiscardRectangleEXT',
        'vkCmdSetExclusiveScissorNV',
        'vkCmdSetScissor',
        'vkCmdSetScissorWithCount',
    }
    _output_of_ = {
        'vkGetPhysicalDevicePresentRectanglesKHR',
    }
    _python_name_ = {
        'offset': 'offset',
        'extent': 'extent',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkRect2D._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
]

VkRect2D._type_ = {
    'offset': VkOffset2D,
    'extent': VkExtent2D,
}
