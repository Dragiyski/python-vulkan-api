import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
        'VkOffset2D',
    },
    'included_in': {
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
    },
    'input_of': {
        'vkCmdSetDiscardRectangleEXT',
        'vkCmdSetExclusiveScissorNV',
        'vkCmdSetScissor',
        'vkCmdSetScissorWithCount',
    },
    'output_of': {
        'vkGetPhysicalDevicePresentRectanglesKHR',
    },
    'member_map': {
        'offset': {'python_name': ['offset'], 'type': 'VkOffset2D'},
        'extent': {'python_name': ['extent'], 'type': 'VkExtent2D'},
    }
}
