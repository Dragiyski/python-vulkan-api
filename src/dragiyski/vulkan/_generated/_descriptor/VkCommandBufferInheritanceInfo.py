from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCommandBufferInheritanceInfo'
_member_list_ = ['sType', 'pNext', 'renderPass', 'subpass', 'framebuffer', 'occlusionQueryEnable', 'queryFlags', 'pipelineStatistics']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'renderPass': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subpass': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'framebuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'occlusionQueryEnable': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queryFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkQueryControlFlags',
        'enum': 'VkQueryControlFlags',
        'is_string': False,
    },
    'pipelineStatistics': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkQueryPipelineStatisticFlags',
        'enum': 'VkQueryPipelineStatisticFlags',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkAttachmentSampleCountInfoAMD',
    'VkCommandBufferInheritanceConditionalRenderingInfoEXT',
    'VkCommandBufferInheritanceRenderPassTransformInfoQCOM',
    'VkCommandBufferInheritanceRenderingInfo',
    'VkCommandBufferInheritanceViewportScissorInfoNV',
    'VkExternalFormatANDROID',
    'VkMultiviewPerViewAttributesInfoNVX',
    'VkRenderingAttachmentLocationInfoKHR',
    'VkRenderingInputAttachmentIndexInfoKHR',
}
_includes_ = set()
_included_in_ = {
    'VkCommandBufferBeginInfo',
}
_input_of_ = set()
_output_of_ = set()
