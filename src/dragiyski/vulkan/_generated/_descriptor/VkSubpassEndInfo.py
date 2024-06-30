from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubpassEndInfo'
_member_list_ = ['sType', 'pNext']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBPASS_END_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkSubpassFragmentDensityMapOffsetEndInfoQCOM',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdEndRenderPass2',
    'vkCmdNextSubpass2',
}
_output_of_ = set()
