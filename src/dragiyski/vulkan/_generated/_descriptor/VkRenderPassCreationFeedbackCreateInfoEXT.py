from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkRenderPassCreationFeedbackCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'pRenderPassFeedback']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_FEEDBACK_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pRenderPassFeedback': {
        'type': CPointerType(CComplexType('VkRenderPassCreationFeedbackInfoEXT')),
        'type_name': 'VkRenderPassCreationFeedbackInfoEXT',
        'structure': 'VkRenderPassCreationFeedbackInfoEXT',
        'is_string': False,
    },
}
_extends_ = {
    'VkRenderPassCreateInfo2',
}
_extended_by_ = set()
_includes_ = {
    'VkRenderPassCreationFeedbackInfoEXT',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
