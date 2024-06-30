from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRect2D'
_member_list_ = ['offset', 'extent']
_member_info_ = {
    'offset': {
        'type': CComplexType('VkOffset2D'),
        'type_name': 'VkOffset2D',
        'structure': 'VkOffset2D',
        'is_string': False,
    },
    'extent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
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
