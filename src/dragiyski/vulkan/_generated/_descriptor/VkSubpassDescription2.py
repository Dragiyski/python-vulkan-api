from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassDescription2'
_member_list_ = ['sType', 'pNext', 'flags', 'pipelineBindPoint', 'viewMask', 'inputAttachmentCount', 'pInputAttachments', 'colorAttachmentCount', 'pColorAttachments', 'pResolveAttachments', 'pDepthStencilAttachment', 'preserveAttachmentCount', 'pPreserveAttachments']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSubpassDescriptionFlags',
        'enum': 'VkSubpassDescriptionFlags',
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'viewMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'inputAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pInputAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
        'length': [['inputAttachmentCount']],
        'is_string': False,
    },
    'colorAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'pResolveAttachments': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'pDepthStencilAttachment': {
        'type': CPointerType(CComplexType('VkAttachmentReference2')),
        'type_name': 'VkAttachmentReference2',
        'structure': 'VkAttachmentReference2',
        'is_string': False,
    },
    'preserveAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPreserveAttachments': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['preserveAttachmentCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkFragmentShadingRateAttachmentInfoKHR',
    'VkMultisampledRenderToSingleSampledInfoEXT',
    'VkRenderPassCreationControlEXT',
    'VkRenderPassSubpassFeedbackCreateInfoEXT',
    'VkSubpassDescriptionDepthStencilResolve',
}
_includes_ = {
    'VkAttachmentReference2',
}
_included_in_ = {
    'VkRenderPassCreateInfo2',
}
_input_of_ = set()
_output_of_ = set()
