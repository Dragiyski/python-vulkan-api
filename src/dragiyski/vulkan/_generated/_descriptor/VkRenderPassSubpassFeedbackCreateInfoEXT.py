from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassSubpassFeedbackCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'pSubpassFeedback']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_SUBPASS_FEEDBACK_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSubpassFeedback': {
        'type': CPointerType(CComplexType('VkRenderPassSubpassFeedbackInfoEXT')),
        'type_name': 'VkRenderPassSubpassFeedbackInfoEXT',
        'structure': 'VkRenderPassSubpassFeedbackInfoEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkSubpassDescription2',
}
_extended_by_ = set()
_includes_ = {
    'VkRenderPassSubpassFeedbackInfoEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
