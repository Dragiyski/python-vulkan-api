from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderingInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'renderArea', 'layerCount', 'viewMask', 'colorAttachmentCount', 'pColorAttachments', 'pDepthAttachment', 'pStencilAttachment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDERING_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkRenderingFlags',
        'enum': 'VkRenderingFlags',
        'is_string': False,
    },
    'renderArea': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
    'layerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'viewMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'colorAttachmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pColorAttachments': {
        'type': CPointerType(CComplexType('VkRenderingAttachmentInfo')),
        'type_name': 'VkRenderingAttachmentInfo',
        'structure': 'VkRenderingAttachmentInfo',
        'length': [['colorAttachmentCount']],
        'is_string': False,
    },
    'pDepthAttachment': {
        'type': CPointerType(CComplexType('VkRenderingAttachmentInfo')),
        'type_name': 'VkRenderingAttachmentInfo',
        'structure': 'VkRenderingAttachmentInfo',
        'is_string': False,
    },
    'pStencilAttachment': {
        'type': CPointerType(CComplexType('VkRenderingAttachmentInfo')),
        'type_name': 'VkRenderingAttachmentInfo',
        'structure': 'VkRenderingAttachmentInfo',
        'is_string': False,
    },
}
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
