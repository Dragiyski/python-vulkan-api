from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassBeginInfo'
_member_list_ = ['sType', 'pNext', 'renderPass', 'framebuffer', 'renderArea', 'clearValueCount', 'pClearValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO',
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
    'framebuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'renderArea': {
        'type': CComplexType('VkRect2D'),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'is_string': False,
    },
    'clearValueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pClearValues': {
        'type': CPointerType(CComplexType('VkClearValue')),
        'type_name': 'VkClearValue',
        'union': 'VkClearValue',
        'length': [['clearValueCount']],
        'is_string': False,
    },
}
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
